#!/bin/bash
app_dir="DIwebsite-redesign"
deploy_branch="fix/travis_autodeploy"
docker_volume_name="diwebsite_db"

printf "Tearing currently deployed images \n\n"
cd $app_dir

echo "DATABASE_URL=postgresql://di_website:di_website_pw@db/di_website" > .env

docker-compose ps -a
docker-compose down

# Move back to root director
printf  "Cloning new content from active branch "$deploy_branch"\n\n"
cd ~
rm -rf $app_dir
git clone git@github.com:devinit/DIwebsite-redesign.git -b $deploy_branch

printf "Starting up services.... \n\n"
cd $app_dir

printf  "Checking if docker database volume exists .... \n\n"

volume_status=$(docker volume ls)

printf $volume_status

if [ grep $docker_volume_name $volume_status ];then
    printf  "Volume already exists, skipping creation of new volume\n\n"
else
   printf  "No docker volume found, creating new volume for deployment\n\n"
   docker volume create --name=$docker_volume_name
fi

echo "DATABASE_URL=postgresql://di_website:di_website_pw@db/di_website" > .env

docker-compose up -d --build