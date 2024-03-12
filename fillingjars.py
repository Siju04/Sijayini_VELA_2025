'''
filling jars
'''
#!/bin/python3

import math
import os
import random
import re

def solve(n, operations):
    total_candies = 0
    for operation in operations:
        a, b, k = operation 
        jars_affected = b - a + 1  
        candies_added = k * jars_affected  
        total_candies += candies_added 

    average = total_candies // n 
    return average  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()
