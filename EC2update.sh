#!/bin/bash
echo "updating EC2 instance..."

ssh-agent bash -c 'ssh-add ~/Downloads/ec2.pem; git push django_test.com +master:refs/heads/master'

# eg.
# ssh -i ~/Downloads/ec2.pem ubuntu@ec2-54-213-195-214.us-west-2.compute.amazonaws.com
