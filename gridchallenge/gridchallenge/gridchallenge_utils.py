import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    for j in range(len(grid[0])):
        for i in range(1,len(grid)):
            if grid[i][j]<grid[i-1][j]:
                return 'NO'
    return 'YES'