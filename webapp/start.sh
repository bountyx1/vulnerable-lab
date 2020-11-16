#!/bin/bash
python3 /root/manage.py runserver &
nginx
echo 1 && tail -f /dev/null
