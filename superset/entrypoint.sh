#!/bin/bash


superset db upgrade
superset fab create-admin \
    --username admin \
    --firstname nguyen \
    --lastname huan \
    --email huannguyen.09.pt@gmail.com \
    --password admin

superset init

superset run -h 172.20.1.5 -p 8088 --with-threads --reload --debugger

# exec /bin/bash
tail -f /dev/null
