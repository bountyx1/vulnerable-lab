FROM ubuntu
RUN apt-get update  && apt-get install wget -y && apt-get clean
RUN wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-core-7.0.0-x64.bin -O /tmp/jira.bin
RUN cd /tmp && chmod +x jira.bin && printf "%s\n" "o" "1" "i" | ./jira.bin  
expose 8080
COPY start.sh /root/start.sh 
RUN chmod +x /root/start.sh
CMD ["/root/start.sh"]
