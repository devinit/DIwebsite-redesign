#!/bin/bash
working_directory=/home/di_website/DIwebsite-redesign
#If successful copy certs to the correct folder and refresh nginx docker node
cd $working_directory
cp -f  /etc/letsencrypt/live/devinit.org/privkey.pem ssl/
cp -f /etc/letsencrypt/live/devinit.org/fullchain.pem ssl/

command docker-compose exec nginx  nginx -s  reload
