def lambda_handler(event, context):
    print("여기서 시작")
    print("Jane")
    print("again")
    return {
        'statusCode': 200,
        'body': 'Hello from my toy Lambda function!'
    }