"""
Lab4-Q2G: Retrieve a bucket policy
"""
import boto3

bucket_name = 'jihyelab42abuc'
s3 = boto3.client('s3')
response = s3.get_bucket_acl(Bucket=bucket_name)
print (response)