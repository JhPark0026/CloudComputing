"""
Lab4-Q3F: Batch write to a table
"""
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jihyelab4')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'account_type': 'standard_user',
            'username': 'kkobiryu',
            'first_name': 'Kkobi',
            'last_name': 'Ryu',
            'age': 21,
            'address': {
                'road': '25 Samsan',
                'city': 'Ulsan',
                'state': 'Nam-Gu'
            }
        }
    )
    batch.put_item(
        Item = {
            'account_type': 'super_user',
            'username': 'brownkim',
            'first_name': 'Brown',
            'last_name': 'Kim',
            'age': 14,
            'address': {
                'road': '13 Samsan',
                'city': 'Ulsan',
                'state': 'Nam-Gu'
            }
        }
    )
    batch.put_item(
        Item = {
            'account_type': 'standard_user',
            'username': 'sarangjo',
            'first_name': 'Sarang',
            'last_name': 'Jo',
            'age': 45,
            'address': {
                'road': '25 Shincheon',
                'city': 'Ulsan',
                'state': 'Buk-Gu'
            }
        }
    )