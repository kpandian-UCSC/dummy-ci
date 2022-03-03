'''
Implementation of Module 1
'''

import json
import os

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    env = os.environ.get('MY_ENV')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda Deploy from same lambda' + env)
    }
