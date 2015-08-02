#!/usr/bin/env bash

#
# =======================
# provision shell script
# =======================
#

sudo apt-get -y update

echo 'Installing git ...'
sudo apt-get -y install git

echo 'Installing python libraries ...'
sudo apt-get -y install build-essential python-dev
sudo pip install --upgrade pip
sudo pip install python-axolotl
sudo apt-get -y install python-setuptools python-pip

echo 'Installing Django ...'
sudo pip install Django==1.8.3
sudo pip install djangorestframework

sudo apt-get -y install libjpeg-dev libpng-dev
sudo apt-get -y python-imaging
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
sudo pip install pillow


# Database
#sudo apt-get -y install python-psycopg2
#sudo apt-get -y install postgresql postgresql-contrib
#sudo apt-get -y install libpq-dev