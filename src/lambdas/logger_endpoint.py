'''Module for Logging Request Input and Output '''
import json

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    return {
        'statusCode': 200,
        'body': json.dumps("This is going to Log to Lambda")
    }
