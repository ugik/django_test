#!/bin/bash
#
# instantiate EC2 Ubuntu Server 12.04.3 LTS - ami-6aad335a (64-bit)
# save ssh key to ~/Downloads as ec2.pem
# mysqldump -u root -p[root_password] [database_name] > data.sql
#
echo "copying to EC2 instance..."
if [[ "$2" == "" ]]
	then echo "usage: bash EC2start {host-name} {setup-script}"
    else echo 'setup script"$2"'		#scp -i ~/Downloads/ec2.pem data.sql ubuntu@"$1":data.sql
		scp -i ~/Downloads/ec2.pem EC2setup.sh ubuntu@"$1":"$2"
		ssh -i ~/Downloads/ec2.pem ubuntu@"$1" bash "$2"
fi

# eg.
# bash EC2start ec2-54-213-239-72.us-west-2.compute.amazonaws.com
# ssh -i ~/Downloads/ec2.pem ubuntu@ec2-54-213-239-72.us-west-2.compute.amazonaws.com
# scp -i ~/Downloads/ec2.pem foo.file ubuntu@ec2-54-213-239-72.us-west-2.compute.amazonaws.com

