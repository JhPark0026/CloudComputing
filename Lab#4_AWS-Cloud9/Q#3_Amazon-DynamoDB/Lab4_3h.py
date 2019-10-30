"""
Lab4-Q3H: Delete a table
"""
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

table.delete()