import boto3
from boto3.dynamodb.conditions import Key, Attr

# DynamoDB 리소스 생성
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventory')  # 실제 테이블 이름으로 변경 필요

def create_item(item_id, name, quantity):
    """새 항목을 추가합니다."""
    response = table.put_item(
        Item={
            'item_id': item_id,
            'name': name,
            'quantity': quantity
        }
    )
    return response

def read_item(item_id):
    """특정 item_id에 해당하는 항목을 조회합니다."""
    response = table.get_item(
        Key={'item_id': item_id}
    )
    return response.get('Item')

def update_item(item_id, quantity):
    """item_id의 수량을 업데이트합니다."""
    response = table.update_item(
        Key={'item_id': item_id},
        UpdateExpression='SET quantity = :val',
        ExpressionAttributeValues={':val': quantity},
        ReturnValues='UPDATED_NEW'
    )
    return response

def delete_item(item_id):
    """item_id에 해당하는 항목을 삭제합니다."""
    response = table.delete_item(
        Key={'item_id': item_id}
    )
    return response
