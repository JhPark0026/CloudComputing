"""
Lab4-Q1G: Delete an existing key pair
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName='jihyeLab41fKey')
print('Success', response)
