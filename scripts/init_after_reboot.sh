#!/usr/bin/bash

key_value_store=http://consul:8500/v1/kv/deploy/backend
blue_upstream=http://blue
green_upstream=http://green

# Sleep for a minute to be sure docker started services
sleep 60
# Set currently running container to new state
echo 'Check the current state'
blue_is_run=$(docker exec blue echo 'yes' 2> /dev/null || echo 'no')
state='green'
new_state='blue'
new_upstream=${blue_upstream}
if [[ ${blue_is_run} != 'yes' ]]
then
    state='blue'
    new_state='green'
    new_upstream=${green_upstream}
fi

./scripts/activate.sh ${new_state} ${state} ${new_upstream} ${key_value_store}
