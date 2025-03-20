def lambda_handler(event, context):
    print("여기서 시작")
    return {
        'statusCode': 200,
        'body': '성공!'
    }