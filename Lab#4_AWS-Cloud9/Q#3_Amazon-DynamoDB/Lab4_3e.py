"""
Lab4-Q3D: Delete an item
"""
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

table.delete_item(
    Key = {
        'username': 'jihyepark',
        'last_name': 'Park'
    }
)