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
ENVIROMENT_VARIABLES='ENVIRONMENT;SECRET_KEY;DEFAULT_FROM_EMAIL;EMAIL_HOST;EMAIL_BACKEND;EMAIL_HOST_USER;EMAIL_HOST_PASSWORD;DATABASE_URL;BRANCH;GITHUB_TOKEN;SITE_URL;WWW_SITE_URL;DATA_SITE_URL;USE_SPACES;AWS_S3_ENDPOINT_URL;AWS_STORAGE_BUCKET_NAME;AWS_ACCESS_KEY_ID;AWS_SECRET_ACCESS_KEY'

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

    start_new_process 'Setting up new docker storage for postgres'
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

function search_reindex {

    start_new_process "Re-indexing search"
    cd $APP_DIR
    sleep 60s
    docker-compose exec -T ${new_state} python manage.py update_index

}

function perform_git_operations {

    start_new_process "Performing git operation on branch $ACTIVE_BRANCH of repository $REPOSITORY"

    if [ -d $APP_DIR ]; then
        cd $APP_DIR

        if [[ $ACTIVE_BRANCH == *"refs/tags"* ]]
        then
            {
                log "Cloning new content from a release tag "$ACTIVE_BRANCH
                git fetch --tags -f
                git stash
                git checkout $ACTIVE_BRANCH
                } || {
                log "Failed to update from git repository"
                exit 20;
            }
        else
            {
                log  "Cloning new content from active branch "$ACTIVE_BRANCH
                git fetch
                git stash
                git checkout $ACTIVE_BRANCH
                git reset --hard origin/$ACTIVE_BRANCH
                } || {
                log "Failed to update from git repository"
                exit 20;
            }
        fi
    else
        {
            git clone -b $ACTIVE_BRANCH $REPOSITORY

            } || {
            log "Failed to perform git clone on $REPOSITORY with branch $ACTIVE_BRANCH "
            exit 20;
        }
    fi
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

    # install JS dependencies
    echo "Update JS dependencies"
    npm ci
    npm run build

    # Attempt to stop new container. Sometimes there is a hanging one still running...
    docker-compose stop ${new_state}
    # update the new state container
    echo "Update the ${new_state} container"
    docker-compose up -d ${new_state}

    # Check the new state container is ready
    echo "Check the ${new_state} container is ready"
    docker-compose run --rm --entrypoint /bin/bash ${new_state} ./scripts/wait-for-it.sh ${new_state}:8090 --timeout=60
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
    sudo chown -R di_website:di_website ssl
    cp certbot_success.sh ./ssl
    chmod +x ssl/certbot_success.sh
    sudo chown -R di_website:di_website certbot_logs
    #run this script within this subprocess
    chmod +x scripts/*
    source scripts/init.sh
    docker-compose -f docker-compose-consul.yml up -d
    setup_blue_green_deployment
    search_reindex

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
