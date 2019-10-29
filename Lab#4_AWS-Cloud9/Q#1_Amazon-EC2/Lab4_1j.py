"""
Lab4-Q1J: Delete an existing security group
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.delete_security_group(GroupId = 'sg-076b9ea48b2e67d7b')
    print('Success', response)
except ClientError as e:
    print(e)
