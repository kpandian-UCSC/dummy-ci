'''
Implementation of Module 1
'''

import json

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    return {
        'statusCode': 200,
        'body': json.dumps('Hello To Yall!')
    }