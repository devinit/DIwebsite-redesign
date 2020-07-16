#!/bin/bash
working_directory=/home/di_website/DIwebsite-redesign
renewal_result="$(command certbot renew  --webroot -w "$working_directory"/letsencrypt)"
#Check if successful result is received
result="$(echo $renewal_result | grep -o Congratulations )"

#If successful copy certs to the correct folder and refresh nginx docker node
if [ $result ]; then
    cd $working_directory
    cp -f  /etc/letsencrypt/live/devinit.org/privkey.pem ssl/
    cp -f /etc/letsencrypt/live/devinit.org/fullchain.pem ssl/

    command docker-compose exec nginx  nginx -s  reload
fi
