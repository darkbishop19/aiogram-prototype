import os

import aioboto3
from boto3.dynamodb.conditions import Attr
from dotenv import load_dotenv

# load_dotenv()


session = aioboto3.Session()
telegram_db = session.resource(
    'dynamodb',
    endpoint_url=os.getenv('USER_STORAGE_URL'),
    region_name=os.getenv('ru-central1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

table_user = 'bot-users'


async def get_username(user_id):
    async with session.resource('dynamodb', endpoint_url=os.getenv('USER_STORAGE_URL'),
                                region_name='ru-central1',
                                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')) as telegram_db:
        table = await telegram_db.Table(table_user)
        scan = await table.scan(FilterExpression=Attr('id_user').eq(user_id))
        return scan['Items'][-1]['username']
