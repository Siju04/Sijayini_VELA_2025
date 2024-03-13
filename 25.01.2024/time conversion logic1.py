''
TIME CONVERSION
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    period = s[-2:]

    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    return f'{hour:02}:{minute:02}:{second:02}'

# Sample Input
print(timeConversion("07:05:45PM"))  # Output: 19:05:45

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
