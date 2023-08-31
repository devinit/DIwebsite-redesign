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

        echo "DATABASE_URL=postgresql://di_website:di_website_pw@db/di_website" > .env

5. Install python dependencies

        pip install -r requirements.txt

6. Install node dependencies

        npm install

7. Build JS

        npm run build

8. Migrate

        python3 manage.py migrate

10. Add

        export DJANGO_SETTINGS_MODULE=di_website.settings.dev

   to your activate file inside

        path_to_virtual_env_folder/bin/

11. Build static assets - refer to *Pattern library* section, then in the project root

        python3 manage.py collectstatic

12. Run

        python3 manage.py runserver

13. Test

        python3 manage.py test

## Develop with Docker

**Install dependencies**

- [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

Run `docker-compose` with the `docker-compose.minimal.yml` file, as below

        docker-compose -f docker-compose.minimal.yml up --build

**Steps to develop with docker:**

1. Create docker volume diwebsite_db
    ```docker
    docker volume create --name=diwebsite_db
    ```
2. Run command:

        docker-compose -f docker-compose.dev.yml up --build

3. You'll need to manually run migrations:

        docker-compose exec web python manage.py migrate

4. If you wish to test the production build, run:

        docker-compose up --build -d

#### *Note*
If the deployment is from scratch, follow commands below to update content with old website content
1. Create pages Publication Index and Blog Index
2. Execute the commands below to finish the migration

   ```docker
   docker-compose exec web python manage.py fixblogs
   docker-compose exec web python manage.py importwp
   docker-compose exec web python manage.py update_index
   ```

## For Spotlights
1. Fetch data from the old CMS repo

        python3 manage.py fetch_spotlight_data

2. Process downloaded files and import data into your database

        python3 manage.py import_spotlight_data

3. If you'd added Spotlight data in one environment and wish to import it into the current one

        python3 manage.py update_spotlights_from_api base_url=[Specify Source URL]
    NB: default base_url is http://178.128.102.213/


## For Custom Widgets

The development environment has been setup using grunt, webpack & typescript.

Widget code sits in the `src` directory. Update the `webpack.config.js` with your widget's configuration then run:

        npm run dev

To bundle your code, run:

        npm run build

## Deployment from scratch notes

```
# Upgrade general dependencies
apt update
apt upgrade

# Install docker
sudo snap refresh && sudo snap install docker

# Install docker ce and compose
apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start docker daemon
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# Enable docker logrotate
nano /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
systemctl restart docker.service

# Turn on firewall
ufw allow 80
ufw allow 443
ufw allow 22
ufw enable

# Create user and add to docker group
adduser di_website
groupadd docker
usermod -aG docker di_website

# Install npm
apt install npm

# Set up containers
su di_website
cd ~
git clone https://github.com/devinit/DIWebsite-redesign.git

APP_NAME="DIwebsite-redesign"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
APP_DIR=$SCRIPT_DIR'/'$APP_NAME
DATABASE_BACKUP=$SCRIPT_DIR'/database_backup'
DATABASE_NAME='di_website'
DOCKER_STORAGE='diwebsite_db;index_db'
REPOSITORY="git@github.com:devinit/"$APP_NAME".git"

cat "$APP_DIR/config/nginx/django_https.ctmpl" >> $APP_DIR"/config/nginx/django.conf.ctmpl"

cd ~/DIWebsite-redesign

chmod +x scripts/*

cd ssl
openssl genrsa > privkey.pem
openssl req -new -x509 -key privkey.pem > fullchain.pem

cd ..

docker pull gliderlabs/registrator:latest
docker network create "consul"

docker-compose -f docker-compose-consul.yml up -d
new_state='blue'
docker build . -t diwebsite-redesign_web:new
docker tag diwebsite-redesign_web:new diwebsite-redesign_web:${new_state}
state='green'
docker tag diwebsite-redesign_web:new diwebsite-redesign_web:${state}
docker volume create --name=diwebsite_db
docker-compose up -d ${new_state}
docker-compose exec -T db psql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
docker-compose exec -T db psql -U di_website -d di_website < ../2023-08-09.backup
docker-compose down

source scripts/init.sh
docker-compose stop green
docker-compose exec -T ${new_state} python manage.py update_index

new_upstream=${blue_upstream}
./scripts/activate.sh ${new_state} ${state} ${new_upstream} ${key_value_store}

docker-compose restart nginx

```

###

If you accidentally have multiple IP addresses for one service in Consul (e.g. stopped service while consul was down)

First, bash into nginx, then `curl -sX GET http://consul:8500/v1/catalog/service/blue` to get the ServiceId.  Followed by `docker-compose -f docker-compose-consul.yml exec consul consul services deregister -id=c06d9f779d7a:blue:8090`
