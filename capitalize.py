You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
 
1
#!/bin/python3
2
?
3
import math
4
import os
5
import random
6
import re
7
import sys
8
# 
9
def solve(s):
10
    for x in s[:].split():
11
        s = s.replace(x, x.capitalize())
12
    return s
13
?
14
if __name__ == '__main__':
15
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
16
?
17
    s = input()
18
?
19
    result = solve(s)
20
?
21
    fptr.write(result + '\n')
22
?
23
    fptr.close()