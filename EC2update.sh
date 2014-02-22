#!/bin/bash
echo "updating EC2 instance..."

ssh -i ~/Downloads/ec2.pem ubuntu@"$1" bash updater.sh

# eg.
# ssh -i ~/Downloads/ec2.pem ubuntu@ec2-54-213-195-214.us-west-2.compute.amazonaws.com
