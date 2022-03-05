''' Module for Unit Testing '''
from src.secrets.manager import get_lambda_secret

def test_addition():
    ''' Testing an Addition '''
    assert 1+2 == 3

def test_get_lambda_secret():
    '''Testing Secret Function'''
    assert get_lambda_secret("key") == "a key"
