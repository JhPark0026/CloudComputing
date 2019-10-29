"""
Lab4-Q1H: Get info about security groups
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds=['sg-0b427ed23ceff26ff'])
    print('Success', response)
except ClientError as e:
    print(e)
