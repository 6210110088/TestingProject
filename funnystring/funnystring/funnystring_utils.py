#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
cha = string.ascii_lowercase

def funnyString(s):
    # Write your code here
    result = 'Funny'
    r = s[::-1]
    
    for idx in range(1, len(s)):
        if abs(cha.index(s[idx]) - cha.index(s[idx-1])) != abs(cha.index(r[idx]) - cha.index(r[idx-1])):
            result = 'Not Funny'
            break
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
