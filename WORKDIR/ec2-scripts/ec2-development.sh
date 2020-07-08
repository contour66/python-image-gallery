#!/usr/bin/bash



yum -y update
amazon-linux-extras install -y nginx1
amazon-linux-extras install -y java-openjdk11
yum install -y java-11-openjdk-devel
yum install -y git python3  postgresql postgresql-devel gcc python3-devel
yum install -y emacs-nox nano tree


# Configure/install custom software
cd /home/ec2-user
git clone https://github.com/contour66/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"

# Start/enable services
systemctl stop postfix
systemctl disable postfix
