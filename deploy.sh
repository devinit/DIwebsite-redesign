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
    PROJECTNAME=$(docker ps --format "table {{.ID}}  {{.Names}}  {{.CreatedAt}}" | grep db | tail -n 1 | awk -F  "  " '{print $2}' | cut -d"_" -f1)
    docker-compose --project-name=$PROJECTNAME exec -T db pg_dump -U di_website -d di_website >  $file_name

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

    docker-compose --project-name=$ENV exec -T web python manage.py update_index

}

function perform_git_operations {

    start_new_process "Performing git operation on branch $ACTIVE_BRANCH of repository $REPOSITORY"

    if [ -d $APP_DIR ]; then
        cd $APP_DIR

        {
            # Move back to root director
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

    until docker-compose --project-name=$ENV exec -T rabbitmq rabbitmqctl start_app; do
        log "Rabbit is unavailable - sleeping"
        sleep 10
    done

    docker-compose --project-name=$ENV exec -T rabbitmq rabbitmqctl add_user di_website $RABBITMQ_PASSWORD
    docker-compose --project-name=$ENV exec -T rabbitmq rabbitmqctl add_vhost myvhost
    docker-compose --project-name=$ENV exec -T rabbitmq rabbitmqctl set_user_tags di_website di_website
    docker-compose --project-name=$ENV exec -T rabbitmq rabbitmqctl set_permissions -p myvhost di_website ".*" ".*" ".*"

    start_new_process "Starting celery"
    docker-compose --project-name=$ENV exec -T web chown root '/etc/default/celeryd'
    docker-compose --project-name=$ENV exec -T web chmod 640 '/etc/default/celeryd'
    docker-compose --project-name=$ENV exec -T web /etc/init.d/celeryd start

    log "Finished setting up link checker .."

}

function enable_https_configs {

    if [ "$ENVIRONMENT" == 'production' ]; then
        echo 'include /etc/nginx/conf.d/django_https;' >> $APP_DIR"/config/nginx/django.conf"
    fi
}

function build_with_docker_compose {
    if [ $(docker ps -f name=blue -q) ]
    then
        ENV="green"
        OLD="blue"
    else
        ENV="blue"
        OLD="green"
    fi

    echo "Starting "$ENV" container"
    sudo chown -R di_website:di_website core
    docker-compose --project-name=$ENV up -d --build
    docker-compose --project-name=traefik -f traefik/docker-compose.traefik.yml restart traefik

}

if [ ${args[0]} == 'run' ]
then
    if [ -d $APP_DIR ]; then
        backup_database
    fi


    perform_git_operations
    export_travis_enviroment
    setup_docker_storage

    cp $SCRIPT_DIR"/box_config.json" $APP_DIR"/"

    mkdir -p $APP_DIR"/assets"
    mkdir -p $APP_DIR"/storage"

    enable_https_configs

    start_new_process "Starting up services ..."
    cd $APP_DIR
    sudo chown -R di_website:di_website storage
    docker-compose --project-name=traefik -f traefik/docker-compose.traefik.yml up -d
    build_with_docker_compose

    sleep 60;
    start_link_checker_processes
    elastic_search_reindex

    start_new_process "Generating static assets"
    docker-compose --project-name=$ENV exec -T web python manage.py collectstatic --noinput
    sudo chown -R di_website:di_website assets

    echo "Stopping "$OLD" container"
    docker-compose --project-name=$OLD stop
    exit 0

elif [ ${args[0]} == 'backup' ]
then

    backup_database
    exit 0

else

    log "Failed to find operation; Usage: \n$0 run|backup|restoredb <Vars>"
    exit 20

fi
