"""
Lab4-Q3C: Get (retrieve) an item
"""
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

response = table.get_item(
    Key = {
        'username': 'jihyepark',
        'last_name': 'Park'
    })
item = response['Item']
print (item)
