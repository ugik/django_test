#!/bin/bash
# updates ec2 instance

project='django_test'

# fetch repo updates
git init
git remote add origin https://github.com/ugik/$project.git
git fetch --all
git reset --hard origin/master

# update database
cd $project
python manage.py syncdb

# restart Apache
sudo service apache2 restart

