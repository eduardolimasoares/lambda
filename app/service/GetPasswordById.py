import boto3
from botocore.exceptions import ClientError

class GetPasswordById:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_password(self, id):
        try:
            response = self.table.get_item(Key={'id': id})
            password = response.get('password')
            if password:
                return password
            else:
                return None
        except ClientError as e:
            print(f"Erro ao buscar senha do email {email}: {e.response['Error']['Message']}")
            return None