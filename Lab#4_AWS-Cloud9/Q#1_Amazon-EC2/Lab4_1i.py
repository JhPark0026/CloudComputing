"""
Lab4-Q1I: Create a security group to access an Amazon EC2 instance
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.create_security_group(GroupName = 'Lab41I', Description = 'Lab41I created 10/29/19')
    print('Success', response)
except ClientError as e:
    print(e)
