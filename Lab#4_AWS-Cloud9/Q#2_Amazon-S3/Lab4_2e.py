"""
Lab4-Q2E: Create Presigned URLs
"""
import boto3
import logging
bucket_name = 'jihyelab42abuc'
key = 'README.md'
s3 = boto3.client('s3')
response = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket_name, 'Key': key})
print (response)
