'''
Implementation of Module 1
'''

def is_prime(n: int) -> bool:
    '''
    Function Docstring
    '''
    if n <= 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
