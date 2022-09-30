import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

lowerchar = string.ascii_lowercase
upperchar = string.ascii_uppercase

def caesarCipher(s, k):
    # Write your code here
    result = []
    for char in s:
        if char.isupper():
            result.append(upperchar[(upperchar.index(char)+k)%len(upperchar)])
        elif char.islower():
            result.append(lowerchar[(lowerchar.index(char)+k)%len(lowerchar)])
        else:
            result.append(char)
            
    return "".join(map(str, result))