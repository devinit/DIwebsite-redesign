#!/bin/bash
set -E

trap '[ "$?" -ne 20 ] || exit 20' ERR
# trap finalize EXIT

args=("$@")
function perform_git_operations {
    git pull origin
}


function enable_https_configs {
    https_content="listen 443 ssl;"
    if [[ "$ENVIRONMENT" == "production" || "$ENVIRONMENT" == "staging" ]]
    then
        if grep -q "${https_content}" $APP_DIR"/config/nginx/django.conf.ctmpl"; then
            echo "ssl config already exists"
        else
            cat "$APP_DIR/config/nginx/django_https.ctmpl" >> $APP_DIR"/config/nginx/django.conf.ctmpl"
        fi
    fi
}

function setup_blue_green_deployment {
    # build the new Image
    echo 'Build the new image'
    docker build . -t diwebsite-redesign_web:new

    # check the current container state
    echo 'Check the current state'
    blue_is_run=$(docker exec blue echo 'yes' 2> /dev/null || echo 'no')
    state='blue'
    new_state='green'
    new_upstream=${green_upstream}
    if [[ ${blue_is_run} != 'yes' ]]
    then
        state='green'
        new_state='blue'
        new_upstream=${blue_upstream}
    fi

    # create the new state image
    docker tag diwebsite-redesign_web:new diwebsite-redesign_web:${new_state}

    # update the new state container
    echo "Update the ${new_state} container"
    docker-compose up -d ${new_state}

    # Check the new state container is ready
    echo "Check the ${new_state} container is ready"
    docker-compose run --rm --entrypoint /bin/bash ${new_state} ./scripts/wait-for-it.sh ${new_state}:8090 --timeout=60

    #Check the new app
    echo 'Check the new app'
    status=$(docker-compose run --rm nginx curl ${new_upstream}:8090 -o /dev/null -Isw '%{http_code}')
    if [[ ${status} != '200' ]]
    then
        echo "Bad HTTP response in the ${new_state} diwebsite-redesign_web: ${status}"
        chmod +x scripts/reset.sh
        ./scripts/reset.sh ${key_value_store} ${state}
        exit 1
    fi

    chmod +x ./scripts/activate.sh
    ./scripts/activate.sh ${new_state} ${state} ${new_upstream} ${key_value_store}

    echo "Set the ${new_state} image as ${state}"
    docker tag diwebsite-redesign_web:${new_state} diwebsite-redesign_web:${state}

    echo 'Set the old image as previous'
    docker tag diwebsite-redesign_web:latest diwebsite-redesign_web:previous

    echo 'Set the new image as latest'
    docker tag diwebsite-redesign_web:new diwebsite-redesign_web:latest

    echo "Stop the ${state} container"
    docker-compose stop ${state}
}

function main {
    perform_git_operations
    enable_https_configs
    chmod +x scripts/*
    source scripts/init.sh
    docker-compose -f docker-compose-consul.yml up -d
    setup_blue_green_deployment
}

main
