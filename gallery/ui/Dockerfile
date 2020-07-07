FROM ubuntu:18.04
PG_HOST =  ".0.0.0.0"
#PG_PORT -- the port number of the PostgreSQL database,
#IG_DATABASE -- the name of the image gallery PostgreSQL database,
#IG_USER -- the name of the image gallery PostgreSQL user,
#IG_PASSWD -- the password for the image gallery PostgreSQL user,
#IG_PASSWD_FILE -- the full path to a file that contains the image gallery user's password (supersedes IG_PASSWD),
## Install dependencies
#RUN apt-get update && \
# apt-get -y install apache2
#
RUN apt-get update -y && apt-get install python3 -y
COPY createDB.py /app/createDB.py
## Install apache and write hello world message
#RUN echo 'Hello World!' > /var/www/html/index.html
#
## Configure apache
#RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
# echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
# echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \
# echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \
# chmod 755 /root/run_apache.sh
#
#EXPOSE 80


CMD["/usr/bin/python3", "/app/createDB.py"]

