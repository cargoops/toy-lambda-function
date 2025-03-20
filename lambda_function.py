import random

def lambda_handler(event, context):
    # 랜덤 이름 선택
    names = ['Mel', 'Michelle', 'Jane', 'Hyu', 'Edgar']
    name = random.choice(names)

    # prefix 추가
    if name in ['Mel', 'Michelle', 'Jane']:
        name = f'Beautiful {name}'
    else:
        name = f'Handsome {name}'

    # 확인용 로그
    print(name)

    return {
        'statusCode': 200,
        'body': name
    }