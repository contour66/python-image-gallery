FROM ubuntu:latest
#host
ENV PG_HOST =  ".0.0.0.0"
#the port number of the PostgreSQL database,
ENV PG_PORT = "5432"
#the name of the image gallery PostgreSQL database,
ENV IG_DATABASE = "image_gallery"
#the name of the image gallery PostgreSQL user,
ENV IG_USER = "dog"
#password
ENV IG_PASSWD = "cat"
#the full path to a file that contains the image gallery user's password (supersedes IG_PASSWD),
ENV IG_PASSWD_FILE = "/some/path/"
# Install dependencies
#RUN apt-get update && \
# apt-get -y install apache2
#
RUN apt-get update -y && apt-get install python3 -y
RUN useradd -m zamir


COPY --chown=zamir:zamir createDB.py /app/createDB.py
WORKDIR /app
# Boot Command
CMD ["/usr/bin/python3", "createDB.py"]
## Install apache and write hello world message
#RUN echo 'Hello World!' > /var/www/html/index.html
#
## Configure apache
#RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
# echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
# echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \
# echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \
# chmod 755 /root/run_apache.sh
#
#EXPOSE 80




