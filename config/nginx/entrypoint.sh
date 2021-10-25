#!/bin/sh

# Load cronjob to reload webserver
echo "Adding crontab to reload Nginx every 2300 Hours"
service cron start
echo "0 23 * * * nginx -s reload & nginx" | crontab -
