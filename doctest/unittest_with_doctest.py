#!/bin/python3

import math
import os
import random
import re
import sys
import inspect


# Complete the following isPalindrome function:
def isPalindrome(x):
    # Write the doctests:
    """
        >>> isPalindrome(121)
        True
        >>> isPalindrome(344)
        False
        >>> isPalindrome(-121)
        Traceback (most recent call last):
        ...
        ValueError: x must be a positive integer
        >>> isPalindrome("Hello")
        Traceback (most recent call last):
        ...
        ValueError: x must be an integer
    """
    # Write the functionality:
    if(x < 0):
        raise ValueError('x must be a positive integer')
    x = str(x)
    
    if(not x.isdigit()):
        raise ValueError('x must be an integer')
    
    if(x == x[::-1]):
        return True
    else:
        return False
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = input()
    
    if x.isdigit():
        x = int(x)

    res = isPalindrome(x)
    
    doc = inspect.getdoc(isPalindrome)
    
    func_count = len(re.findall(r'isPalindrome', doc))
    true_count = len(re.findall(r'True', doc))
    false_count = len(re.findall(r'False', doc))
    pp_count = len(re.findall(r'>>>', doc))
    trace_count = len(re.findall(r'Traceback', doc))

    fptr.write(str(res)+'\n')
    fptr.write(str(func_count)+'\n')
    fptr.write(str(true_count)+'\n')
    fptr.write(str(false_count)+'\n')
    fptr.write(str(pp_count) + '\n')
    fptr.write(str(trace_count) + '\n')

    fptr.close()
