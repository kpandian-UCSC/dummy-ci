'''
Amazon Secrets Manager
'''
# import base64
# import boto3
# from botocore.exceptions import ClientError

# pylint: disable=W0613
# pylint: disable=W0611
# pylint: disable=R1720
# pylint: disable=C0103
# pylint: disable=C0301
def get_lambda_secret(secret_name, region_name: str = "us-west-1"):
    '''
    Get Lambda Secret Function
    '''
    return "a key"
    # Create a Secrets Manager client
    # session = boto3.session.Session()
    # client = session.client(
    #     service_name='secretsmanager',
    #     region_name=region_name
    # )

    # try:
    #     get_secret_value_response = client.get_secret_value(
    #         SecretId = secret_name
    #     )
    #     return get_secret_value_response
    # except ClientError as e:
    #     if e.response['Error']['Code'] == 'DecryptionFailureException':
    #         # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
    #         # Deal with the exception here, and/or rethrow at your discretion.
    #         raise e
    #     elif e.response['Error']['Code'] == 'InternalServiceErrorException':
    #         # An error occurred on the server side.
    #         # Deal with the exception here, and/or rethrow at your discretion.
    #         raise e
    #     elif e.response['Error']['Code'] == 'InvalidParameterException':
    #         # You provided an invalid value for a parameter.
    #         # Deal with the exception here, and/or rethrow at your discretion.
    #         raise e
    #     elif e.response['Error']['Code'] == 'InvalidRequestException':
    #         # You provided a parameter value that is not valid for the current state of the resource.
    #         # Deal with the exception here, and/or rethrow at your discretion.
    #         raise e
    #     elif e.response['Error']['Code'] == 'ResourceNotFoundException':
    #         # We can't find the resource that you asked for.
    #         # Deal with the exception here, and/or rethrow at your discretion.
    #         raise e
    # # else:
    # #     # Decrypts secret using the associated KMS CMK.
    # #     # Depending on whether the secret is a string or binary, one of these fields will be populated.
    # #     if 'SecretString' in get_secret_value_response:
    # #         secret = get_secret_value_response['SecretString']
    # #     else:
    # #         decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    # return ""
