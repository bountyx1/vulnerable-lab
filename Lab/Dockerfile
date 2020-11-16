FROM nginx
RUN apt-get update && apt-get install python3 python3-pip -y && apt-get clean
COPY authlab /root
RUN pip3 install -r /root/requirements.txt && python3 /root/manage.py makemigrations && python3 /root/manage.py migrate
COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh
CMD ["/root/start.sh"]
