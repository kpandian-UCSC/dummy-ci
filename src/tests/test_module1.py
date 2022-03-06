''' Module for Unit Testing '''
from lambdas.secrets.manager import get_lambda_secret
from lambdas.lambda_function2 import lambda_handler

def test_addition():
    ''' Testing an Addition '''
    assert 1+2 == 3

def test_lambda2_handler():
    '''Testing Lambda2 Function'''
    assert lambda_handler(0,0) is not None

def test_get_lambda_secret():
    '''Testing Secret Function'''
    assert get_lambda_secret("key_name") != ""
