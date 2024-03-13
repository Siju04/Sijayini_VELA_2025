'''
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

from datetime import datetime

def timeConversion(s):

    dt_object = datetime.strptime(s, '%I:%M:%S%p')

    result = dt_object.strftime('%H:%M:%S')

    return result

print(timeConversion("07:05:45PM"))'''
