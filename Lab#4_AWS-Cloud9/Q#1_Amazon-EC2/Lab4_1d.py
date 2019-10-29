"""
Lab4-Q1D: Reboot Amazon EC2 instance
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['i-02c1f0a64f91cb3fd'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances")
        raise
    # Dry run succeeded, run start_instances again without dryrun
try:
    response = ec2.reboot_instances(InstanceIds=['i-02c1f0a64f91cb3fd'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)
