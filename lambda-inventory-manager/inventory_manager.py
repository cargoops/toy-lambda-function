import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

# DynamoDB 리소스 생성
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventory')  # 실제 테이블 이름 사용

def lambda_handler(event, context):
    action = event.get('action')  # 예: "create", "read", ...
    body = event.get('body') or {}

    if action == 'create':
        return create_item(body['item_id'], body['name'], body['quantity'])
    elif action == 'read':
        return {'statusCode': 200, 'body': json.dumps(read_item(body['item_id']))}
    elif action == 'update':
        return update_item(body['item_id'], body['quantity'])
    elif action == 'delete':
        return delete_item(body['item_id'])
    else:
        return {'statusCode': 400, 'body': 'Invalid action'}

def create_item(item_id, name, quantity):
    response = table.put_item(
        Item={'item_id': item_id, 'name': name, 'quantity': quantity}
    )
    return {'statusCode': 200, 'body': 'Item created'}

def read_item(item_id):
    response = table.get_item(Key={'item_id': item_id})
    return response.get('Item', {})

def update_item(item_id, quantity):
    response = table.update_item(
        Key={'item_id': item_id},
        UpdateExpression='SET quantity = :val',
        ExpressionAttributeValues={':val': quantity},
        ReturnValues='UPDATED_NEW'
    )
    return {'statusCode': 200, 'body': json.dumps(response['Attributes'])}

def delete_item(item_id):
    response = table.delete_item(Key={'item_id': item_id})
    return {'statusCode': 200, 'body': 'Item deleted'}
