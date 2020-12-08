#!/bin/bash
working_directory=/home/di_website/DIwebsite-redesign
command certbot renew  --webroot -w "$working_directory"/letsencrypt --deploy-hook "$working_directory"/certbot_success.sh
