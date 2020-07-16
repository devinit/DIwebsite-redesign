# DIwebsite-redesign
New DI website 2019

## Pattern library

Pattern library imported from https://gitlab.com/the-b-team/development-initiatives-website/ on 12.6.2019.

Pattern library available online at [http://development-initiatives.surge.sh/](http://development-initiatives.surge.sh/)

### Usage

    cd patterns
    nvm install 6.13.0
    nvm exec 6.13.0 npm i
    nvm exec 6.13.0 npm run build

## Dev Setup

1. Create a local database

        psql -U postgres -c 'CREATE DATABASE devinit;'

2. Create a virtual environment

        python3 -m virtualenv venv

3. Source your virtual environment

        source venv/bin/activate

4. Add database URL to the `.env` file. This shall be read by `django-dotenv`

        echo "DATABASE_URL=postgresql://postgres@/devinit" > .env

5. Install python dependencies

        pip install -r requirements.txt

6. Migrate

        python3 manage.py migrate


7. Install Rabbitmq in Ubuntu

        sudo apt-get install rabbitmq-server

8. Add

        export DJANGO_SETTINGS_MODULE=di_website.settings.dev

   to your activate file inside

        path_to_virtual_env_folder/bin/

9. Run Celery worker

        celery -A wagtaillinkchecker worker -l info

10. Build static assets - refer to *Pattern library* section, then in the project root

        python3 manage.py collectstatic

11. Run

        python3 manage.py runserver

12. Test

        python3 manage.py test

## Run with Docker Compose
1. Create docker volume diwebsite_db
    ```docker
    docker volume create --name=diwebsite_db
    ```
2. Run command docker-compose up

#### *Note*
If the deployment is from scratch, follow commands below to update content with old website content
1. Create pages Publication Index and Blog Index
2. Execute the commands below to finish the migration

   ```docker
   docker-compose exec web python manage.py fixblogs
   docker-compose exec web python manage.py importwp
   docker-compose exec web python manage.py update_index
   ```
To enable rabbitmq management
   ```
   docker-compose exec rabbitmq rabbitmq-plugins enable rabbitmq_management
   ```


## For Spotlights
1. Fetch data from the old CMS repo

        python3 manage.py fetch_spotlight_data

2. Process downloaded files and import data into your database

        python3 manage.py import_spotlight_data

3. If you'd added Spotlight data in one environment and wish to import it into the current one

        python3 manage.py update_spotlights_from_api base_url=[Specify Source URL]
    NB: default base_url is http://178.128.102.213/
