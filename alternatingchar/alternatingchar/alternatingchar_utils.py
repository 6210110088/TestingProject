from itertools import count
import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    # Write your code here
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
    return count