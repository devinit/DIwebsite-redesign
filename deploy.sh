#!/bin/bash
app_dir="DIwebsite-redesign"
deploy_branch="develop"
docker_volume_name="diwebsite_db"

printf "Tearing currently deployed images \n\n"
cd $app_dir

echo "DATABASE_URL=postgresql://di_website:di_website_pw@db/di_website" > .env

docker-compose ps -a
docker-compose down

# Move back to root director
printf  "Cloning new content from active branch "$deploy_branch"\n\n"
git fetch
git stash
git checkout $deploy_branch
git reset --hard origin/$deploy_branch

printf "Starting up services.... \n\n"
echo "DATABASE_URL=postgresql://di_website:di_website_pw@db/di_website" > .env
docker-compose up -d --build

