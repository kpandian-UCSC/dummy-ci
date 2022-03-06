'''
Implementation of Module 1
'''

import json
import os
from src.secrets.manager import get_lambda_secret

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    env = os.environ.get('MY_ENV')
    res = get_lambda_secret("test-key")
    return {
        'statusCode': 200,
        'body': json.dumps(
            f'Hello Lambda Deploy from same lambda os: {env}, sm: {res}')
    }
print(lambda_handler(0,0))
