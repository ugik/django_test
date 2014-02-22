#!/bin/bash
echo "setup EC2 instance..."

project='django_test'
project_app=$project"/django_test"

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install apache2 libapache2-mod-wsgi
sudo apt-get -y install python-pip
sudo pip install django
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password mysql'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password mysql'
sudo apt-get -y install mysql-server python-mysqldb
sudo apt-get -y install git-core
git clone https://github.com/ugik/$project.git

sudo rm /etc/apache2/httpd.conf
sudo touch /etc/apache2/httpd.conf
sudo chmod 777 /etc/apache2/*.conf
sudo echo "WSGIScriptAlias / /home/ubuntu/"$project_app"/wsgi.py" >> /etc/apache2/httpd.conf
sudo echo "WSGIPythonPath /home/ubuntu/"$project >> /etc/apache2/httpd.conf
sudo echo "<Directory /home/ubuntu/"$project_app">" >> /etc/apache2/httpd.conf
sudo echo "<Files wsgi.py>" >> /etc/apache2/httpd.conf
sudo echo "<IfVersion < 2.3 >" >> /etc/apache2/httpd.conf
sudo echo "    Order deny,allow" >> /etc/apache2/httpd.conf
sudo echo "    Allow from all" >> /etc/apache2/httpd.conf
sudo echo "</IfVersion>" >> /etc/apache2/httpd.conf
sudo echo "<IfVersion > 2.3 >" >> /etc/apache2/httpd.conf
sudo echo "    Require all granted" >> /etc/apache2/httpd.conf
sudo echo "</IfVersion>" >> /etc/apache2/httpd.conf
sudo echo "</Files>" >> /etc/apache2/httpd.conf
sudo echo "</Directory>" >> /etc/apache2/httpd.conf
sudo echo " " >> /etc/apache2/httpd.conf

sudo echo "<Directory /home/ubuntu/"$project"/static>" >> /etc/apache2/httpd.conf
sudo echo "<Files wsgi.py>" >> /etc/apache2/httpd.conf
sudo echo "<IfVersion < 2.3 >" >> /etc/apache2/httpd.conf
sudo echo "    Order deny,allow" >> /etc/apache2/httpd.conf
sudo echo "    Allow from all" >> /etc/apache2/httpd.conf
sudo echo "</IfVersion>" >> /etc/apache2/httpd.conf
sudo echo "<IfVersion > 2.3 >" >> /etc/apache2/httpd.conf
sudo echo "    Require all granted" >> /etc/apache2/httpd.conf
sudo echo "</IfVersion>" >> /etc/apache2/httpd.conf
sudo echo "</Files>" >> /etc/apache2/httpd.conf
sudo echo "</Directory>" >> /etc/apache2/httpd.conf

sudo echo "Include httpd.conf" >> /etc/apache2/apache2.conf

# copy django admin statics files
cp -r /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/ /home/ubuntu/$project/static

# assumes data.sql for data upload
cd ~
mysql -u root -pmysql -e "create database data; GRANT ALL PRIVILEGES ON data.* TO django@localhost IDENTIFIED BY 'django'"
mysql -u root -pmysql data < data.sql

sudo service apache2 restart

#http://nickpolet.com/blog/1/
#http://www.lleess.com/2013/05/install-django-on-apache-server-with.html#.UwavkDddV38
