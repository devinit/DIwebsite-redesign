#!/bin/bash
set -E

trap '[ "$?" -ne 20 ] || exit 20' ERR
# trap finalize EXIT

args=("$@")

if [ $# -lt 1 ]
then
    printf "Usage: \n$0 run|backup|restoredb <Vars>\n"
    exit 20
fi

# Make sure name matches name used on git and branches being deployed
APP_NAME="DIwebsite-redesign"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
APP_DIR=$SCRIPT_DIR'/'$APP_NAME
DATABASE_BACKUP=$SCRIPT_DIR'/database_backup'
DATABASE_NAME='di_website'
DOCKER_STORAGE='diwebsite_db;index_db'
REPOSITORY="git@github.com:devinit/"$APP_NAME".git"
ACTIVE_BRANCH=$BRANCH
ENVIRONMENT=$ENVIRONMENT
STAGING_IP=
ENVIROMENT_VARIABLES='ENVIRONMENT;SECRET_KEY;DEFAULT_FROM_EMAIL;EMAIL_HOST;EMAIL_BACKEND;EMAIL_HOST_USER;EMAIL_HOST_PASSWORD;HS_API_KEY;HS_TICKET_PIPELINE;HS_TICKET_PIPELINE_STAGE;ELASTIC_USERNAME;ELASTIC_PASSWORD;RABBITMQ_PASSWORD;DATABASE_URL;CELERY_BROKER_URL;ELASTIC_SEARCH_URL;BRANCH'

OIFS=$IFS
IFS=';'


function finalize {
    $IFS=$OIFS
}

function start_new_process {
    printf "\n===================================================================\n"
    printf "$1"
    printf "\n===================================================================\n"
}

function log {
    printf  "$1\n"
}

function setup_docker_storage {

    start_new_process 'Setting up new docker storage for postgres and elastic search'
    docker_volumes="$( docker volume ls )"

    for storage in $DOCKER_STORAGE
    do
        if echo $docker_volumes | grep -q $storage ; then
            log "Docker volume $storage already exits. Skipping ...."
        else
            docker volume create $storage > /dev/null
            log "Created new docker volume $storage with status "$?
        fi
    done

}

function setup_docker_networks {

    start_new_process 'Setting up new external consul network'
    docker_networks="$( docker network ls )"

        if echo $docker_networks | grep -q "consul"; then
            log "Docker network already exists. Skipping ..."
        else
            docker network create consul > /dev/null
            log "Created new docker network consul with status "$?
        fi
}
# This can only happen after project clonning has been done
function export_travis_enviroment {
    start_new_process 'Exporting enviroment variables defined in Travis to .env file'

    rm $APP_DIR'/'.env > /dev/null && touch $APP_DIR'/'.env

    for env in $ENVIROMENT_VARIABLES
    do
        log "Creating $env"
        eval echo $env"="\${$env} >> $APP_DIR'/'.env
    done

}

function backup_database {

    start_new_process "Creating a backup of working database to location $DATABASE_BACKUP"

    mkdir -p $DATABASE_BACKUP && cd $DATABASE_BACKUP

    current_date=`date '+%F'`
    file_name=$DATABASE_BACKUP'/'$current_date'.backup'

    label="$(($(ls -v | grep $current_date | cat -n | wc -l) + 1))"

    if [ -r $current_date'.backup' ];
    then
        log "Moving file old backup to new location $label.$current_date.backup"
        mv -n $current_date'.backup' $label'.'$current_date'.backup'
    fi

    cd $APP_DIR

    log "Starting backup from remote docker machine $(docker-compose ps -q db)"
    docker-compose exec -T db pg_dump -U di_website -d di_website >  $file_name

    log "Database backup completed..."

    if [ -r $file_name ];
    then
        :
    else
        log "Database backup failed, exiting process ... If this is a fresh deployment, delete $APP_DIR folder"
        exit 20;
    fi

}

function elastic_search_reindex {

    start_new_process "Re-indexing elastic search"
    cd $APP_DIR
    sleep 60s
    docker-compose exec -T ${new_state} python manage.py update_index

}

function perform_git_operations {

    start_new_process "Performing git operation on branch $ACTIVE_BRANCH of repository $REPOSITORY"

    if [ -d $APP_DIR ]; then
        cd $APP_DIR

        {
            # Move back to root directory
            log  "Cloning new content from active branch "$ACTIVE_BRANCH
            git fetch
            git stash
            git checkout $ACTIVE_BRANCH
            git reset --hard origin/$ACTIVE_BRANCH
            } || {
            log "Failed to update from git repository"
            exit 20;
        }
    else
        {
            git clone -b $ACTIVE_BRANCH $REPOSITORY

            } || {
            log "Failed to perform git clone on $REPOSITORY with branch $ACTIVE_BRANCH "
            exit 20;
        }
    fi
}


function start_link_checker_processes {

    start_new_process "Creating Rabbit MQ user and vhost for celery"
    cd $APP_DIR

    until docker-compose exec -T rabbitmq rabbitmqctl start_app; do
        log "Rabbit is unavailable - sleeping"
        sleep 10
    done
    if  docker-compose exec -T rabbitmq rabbitmqctl list_users | grep -q "di_website"; then
        log "user already exists. Skipping ..."
    else
        docker-compose exec -T rabbitmq rabbitmqctl add_user di_website $RABBITMQ_PASSWORD
        docker-compose exec -T rabbitmq rabbitmqctl add_vhost myvhost
        docker-compose exec -T rabbitmq rabbitmqctl set_user_tags di_website di_website
        docker-compose exec -T rabbitmq rabbitmqctl set_permissions -p myvhost di_website ".*" ".*" ".*"
    fi
  

    start_new_process "Starting celery"
    docker-compose exec -T ${new_state} chown root '/etc/default/celeryd'
    docker-compose exec -T ${new_state} chmod 640 '/etc/default/celeryd'
    docker-compose exec -T ${new_state} /etc/init.d/celeryd start

    log "Finished setting up link checker .."

}

function enable_https_configs {

    if [ "$ENVIRONMENT" == 'production' ]; then
        cat "/etc/consul-templates/django_https.ctmpl" >> $APP_DIR"/config/nginx/django.conf.ctmpl"       
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

if [ ${args[0]} == 'run' ]
then
    if [ -d $APP_DIR ]; then
        backup_database
    fi


    perform_git_operations
    export_travis_enviroment
    setup_docker_storage
    setup_docker_networks

    cp $SCRIPT_DIR"/box_config.json" $APP_DIR"/"

    mkdir -p $APP_DIR"/assets"
    mkdir -p $APP_DIR"/storage"

    enable_https_configs

    start_new_process "Starting up services ..."
    cd $APP_DIR
    sudo chown -R di_website:di_website storage
    #run this script within this subprocess
    chmod +x scripts/*
    source scripts/init.sh
    docker-compose -f docker-compose-consul.yml up -d 
    setup_blue_green_deployment
    start_link_checker_processes
    elastic_search_reindex

    start_new_process "Generating static assets"
    docker-compose exec -T ${new_state} python manage.py collectstatic --noinput
    sudo chown -R di_website:di_website assets
 
    exit 0


elif [ ${args[0]} == 'backup' ]
then

    backup_database
    exit 0

else

    log "Failed to find operation; Usage: \n$0 run|backup|restoredb <Vars>"
    exit 20

fi
