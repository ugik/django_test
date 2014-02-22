#!/bin/bash
echo "copying to EC2 instance..."

scp -i ~/Downloads/ec2.pem EC2setup.sh ubuntu@"$1":EC2setup.sh
scp -i ~/Downloads/ec2.pem data.sql ubuntu@"$1":data.sql

ssh -i ~/Downloads/ec2.pem ubuntu@"$1" bash EC2setup.sh

# eg.
# ssh -i ~/Downloads/ec2.pem ubuntu@ec2-54-213-195-214.us-west-2.compute.amazonaws.com
