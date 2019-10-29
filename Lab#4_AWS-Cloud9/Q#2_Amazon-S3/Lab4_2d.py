"""
Lab4-Q2D: Download files from an Amazon S3 Bucket
"""
import boto3
import botocore
s3 = boto3.resource('s3')
key = 'README.md'
filename = 'README2.md'
bucket_name = 'jihyelab42abuc'
s3.Bucket(bucket_name).download_file(key,filename)