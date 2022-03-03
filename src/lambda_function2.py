'''
Implementation of Module 1
'''

import json
import requests

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    res = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
    data = json.loads(res.text)
    return {
        'statusCode': 200,
        'body': json.dumps(data["datetime"])
    }
