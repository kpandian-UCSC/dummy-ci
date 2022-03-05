'''
Implementation of Module 1
'''

import json
import os
from secrets.manager import getLambdaSecret

# pylint: disable=W0613
def lambda_handler(event, context):
    ''' Sample Lambda Function'''
    env = os.environ.get('MY_ENV')
    res = getLambdaSecret("MySecret")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda Deploy from same lambda os: {env}, sm: {res}'.format(env=env, res=res))
    }
print(lambda_handler(0,0))