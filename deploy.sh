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
ACTIVE_BRANCH='develop'
STAGING_IP=
ENVIROMENT_VARIABLES='DATABASE_URL;EMAIL_HOST;EMAIL_BACKEND;EMAIL_HOST_USER;EMAIL_HOST_PASSWORD'

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
function setup_docker_storage {
    
    start_new_process 'Setting up new docker storage for postgres and elastic search'
    docker_volumes="$( docker volume ls )"
    
    for storage in $DOCKER_STORAGE
    do
        if echo $docker_volumes | grep -q $storage ; then
            echo "Docker volume $storage already exits. Skipping ...."
        else
            docker volume create $storage > /dev/null
            echo "Created new docker volume $storage witth status "$?
        fi
    done
    
}

# This can only happen after project clonning has been done
function export_travis_enviroment {
    start_new_process 'Exporting enviroment variables defined in Travis to .env file'
    
    rm $APP_DIR'/'.env > /dev/null && touch $APP_DIR'/'.env
    
    for env in $ENVIROMENT_VARIABLES
    do
        eval echo $env"="\${$env} >> $APP_DIR'/'.env
    done
    
}

function backup_database {
    
    start_new_process "Creating a backup of working database to location $"
    
    mkdir -p $DATABASE_BACKUP && cd $DATABASE_BACKUP
    tmpdir='/tmp/dbback00100100'
    
    current_date=`date '+%F'`
    file_name=$DATABASE_BACKUP'/'$current_date'.backup'
    
    label="$(($(ls -v | grep 'test' | cat -n | wc -l) + 1))"
    
    mv -n $f  $tmpdir/label'.'$current_date'.backup'
    
    cd $APP_DIR
    docker-compose exec db pg_dump -U di_website -d di_website >  $file_name
    
    printf "Database backup completed"
    
    if [ -r $file_name ];
    then
        :
    else
        printf "Database backup failed, exiting process ...\n"
        exit 20;
    fi
    
}

function elastic_search_reindex {
    
    start_new_process "Re-indexing elastic search"
    cd $APP_DIR
    
    docker-compose exec web python manage.py update_index
    
}

function perform_git_operations {
    
    start_new_process "Performing git operation on branch $ACTIVE_BRANBCH of repository $REPOSITORY"
    
    if [ -d $APP_DIR ]; then
        cd $APP_DIR
        
        {
            docker-compose down
            # Move back to root director
            printf  "Cloning new content from active branch "$ACTIVE_BRANCH"\n\n"
            git fetch
            git stash
            git checkout $ACTIVE_BRANCH
            git reset --hard origin/$ACTIVE_BRANCH
            } || {
            printf "Failed to update from git repository \n"
            exit 20;
        }
    else
        {
            git clone --branch $ACTIVE_BRANCH $REPOSITORY
            } || {
            printf "Failed to perform git clone on $REPOSITORY with branch $ACTIVE_BRANCH \n"
            exit 20;
        }
    fi
}


function start_link_checker_processes {
    
    start_new_process "Creating Rabbit MQ user and vhost for celery"
    cd $APP_DIR
    
    docker-compose exec rabbit rabbitmqctl add_user di_website $RABBITMQ_PASSWORD
    docker-compose exec rabbit rabbitmqctl add_vhost myvhost
    docker-compose exec rabbitmqctl set_user_tags di_website di_website
    docker-compose exec rabbitmqctl set_permissions -p myvhost di_website ".*" ".*" ".*"
    
    start_new_process "Starting celery"
    
    docker-compose -exec web celery -A wagtaillinkchecker worker -l info &
    
}


if [ ${args[0]} == 'run' ]
then
    if [ -d $APP_DIR ]; then
        backup_database
    fi

    perform_git_operations
    export_travis_enviroment
    setup_docker_storage

    start_new_process "Starting up services ..."
    cd $APP_DIR
    docker-compose up -d --build
    start_link_checker_processes
    elastic_search_reindex

elif [ ${args[0]} == 'backup' ]
then

    backup_database

else

    printf "Failed to find operation; Usage: \n$0 run|backup|restoredb <Vars>\n"
    exit 20

fi
