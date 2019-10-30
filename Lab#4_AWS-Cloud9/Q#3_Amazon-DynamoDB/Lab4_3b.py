"""
Lab4-Q3B: Create a new item
"""
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

table.put_item(
    Item = {
        'username': 'jihyepark',
        'first_name': 'Jihye',
        'last_name': 'Park',
        'age': 'secret',
        'account_type': 'standard_user',
    })