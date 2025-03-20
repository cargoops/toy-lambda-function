import pandas as pd

def lambda_handler(event, context):
    # 예시: 간단한 DataFrame 생성 후 CSV로 변환하여 반환
    data = {
        'Name': ['John', 'Anna', 'Peter'],
        'Age': [29, 23, 35]
    }
    df = pd.DataFrame(data)

    # 확인용 로그
    print(df)

    return {
        'statusCode': 200,
        'body': df.to_csv(index=False)
    }