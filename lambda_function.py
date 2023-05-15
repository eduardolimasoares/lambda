import json
from app.service.GeneratePassword import PasswordGenerator

def lambda_handler(event, context):
    
    httpMethod = event['httpMethod']

    if httpMethod == 'GET':
        request = event['body']
        response = PasswordGenerator.generate_password_data(request)
    
    return {
        'statusCode': 200,
        'body': 'aaa'
    }
