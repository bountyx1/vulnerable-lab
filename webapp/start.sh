#!/bin/bash
export sendgrid="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"
python3 /root/manage.py runserver &
mkdir -p /tmp/nginx/cache
nginx
echo 1 && tail -f /dev/null
