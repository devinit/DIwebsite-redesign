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

7. Build static assets - refer to *Pattern library* section, then in the project root

        python3 manage.py collectstatic

8. Run

        python3 manage.py runserver

## Run with Docker Compose
1. Create docker volume diwebsite_db
    docker volume create --name=diwebsite_db
2. Run command docker-compose up
