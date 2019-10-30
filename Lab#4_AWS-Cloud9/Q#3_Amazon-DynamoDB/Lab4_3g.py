"""
Lab4-Q3G: Query and scan a table
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

response = table.query(
    KeyConditionExpression = Key('username').eq('sarangjo'))
items = response['Items']
print (items)