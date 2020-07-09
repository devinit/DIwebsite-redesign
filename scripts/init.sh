#!/usr/bin/env bash

set -e

key_value_store=http://consul:8500/v1/kv/deploy/backend
blue_upstream=http://blue
green_upstream=http://green

if [[ $(docker images -q diwebsite-redesign_web:latest 2> /dev/null) == '' ]]
then
    echo 'Build a new diwebsite-redesign_web:latest image'
   # cd ..
    docker build . -t diwebsite-redesign_web:latest
   # cd scripts
fi

if [[ $(docker images -q diwebsite-redesign_web:previous 2> /dev/null) == '' ]]
then
    echo 'Build a new diwebsite-redesign_web:previous image'
  #  cd .
    docker build . -t diwebsite-redesign_web:previous
 #   cd scripts
fi

if [[ $(docker exec nginx echo 'yes' 2> /dev/null) == '' ]]
then
    docker tag diwebsite-redesign_web:latest diwebsite-redesign_web:blue
    docker tag diwebsite-redesign_web:latest diwebsite-redesign_web:green
 #   cd .
    docker-compose up --build -d
fi