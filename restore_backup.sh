#!/bin/bash

docker-compose -f docker-compose.dev.yml exec db psql -U di_website -d di_website -c 'drop schema public CASCADE;'
docker-compose -f docker-compose.dev.yml exec db psql -U di_website -d di_website -c 'create schema public;'
docker cp di.backup diwebsite-redesign_db_1:/var/lib/postgresql/data
docker exec diwebsite-redesign_db_1 psql -U di_website -d di_website -f /var/lib/postgresql/data/di.backup
docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
rm di.backup
