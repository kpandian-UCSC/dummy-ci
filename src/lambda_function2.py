'''
Implementation of Module 1
'''

import json
import requests
from src.secrets.manager import get_lambda_secret

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    res = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
    data = json.loads(res.text)
    return {
        'statusCode': 200,
        'body': json.dumps(data["datetime"] + get_lambda_secret("key_name"))
    }
