'''
Implementation of Endpoint 2
'''

import json

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Via Second Lambda Function!')
    }
