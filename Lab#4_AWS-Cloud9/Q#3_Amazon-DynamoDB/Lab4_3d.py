"""
Lab4-Q3D: Update attributes of the item
"""
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

table.update_item(
    Key = {
        'username': 'jihyepark',
        'last_name': 'Park'
    },
    UpdateExpression = 'SET age = :val1',
    ExpressionAttributeValues = {
        ':val1': 'N/A'
    }
)
response = table.get_item(
    Key = {
        'username': 'jihyepark',
        'last_name': 'Park'
    })
item = response['Item']
print (item)
