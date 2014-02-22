#!/bin/bash
# updates ec2 instance

project='django_test'
git init
git remote add origin https://github.com/ugik/$project.git
git fetch --all
git reset --hard origin/master

