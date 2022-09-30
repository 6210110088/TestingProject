import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    charlist = list(set(s))

    valid_ans = ''
    for a in charlist:
        for b in charlist:
            test_str = ''
            for ch in s:
                if (ch == a or ch == b) and a != b:
                    if len(test_str) <= 0 or test_str[-1] != ch:
                        test_str += ch
                    else:
                        test_str = ''
                        break
        
            if len(test_str) > 1 and len(test_str) > len(valid_ans):
                valid_ans = test_str

    return len(valid_ans)