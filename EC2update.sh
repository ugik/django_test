#!/bin/bash
echo "updating EC2 instance..."

ssh-agent bash -c 'ssh-add ~/Downloads/ec2.pem; git push django_test.com +master:refs/heads/master'
ssh -i ~/Downloads/ec2.pem ubuntu@"$1" sudo service apache2 restart

# eg.
# bash EC2update.sh ec2-54-213-239-72.us-west-2.compute.amazonaws.com
