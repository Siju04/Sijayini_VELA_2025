nimesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

Example



The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

Function Description

Complete the solve function in the editor below.

solve has the following parameters:

int n: the number of candy jars
int operations[m][3]: a 2-dimensional array of operations
Returns

int: the floor of the average number of canidies in all jars
Input Format

The first line contains two integers,  and , separated by a single space.
 lines follow. Each of them contains three integers, , , and , separated by spaces.

Constraints





Sample Input

STDIN       Function
-----       --------
5 3         n = 5, operations[] size = 3
1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100
Sample Output

160
Explanation

Initially each of the jars contains 0 candies

0 0 0 0 0  
First operation:

100 100 0 0 0  
Second operation:

100 200 100 100 100  
Third operation:

100 200 200 200 100  
Total = 800, Average = 800/5 = 160
1
def solve(n, operations):
2
    total_candies = 0
3
​
4
    for operation in operations:
5
        a, b, k = operation
6
        total_candies += (b - a + 1) * k
7
​
8
    average = total_candies // n
9
    return average
10
n, m = map(int, input().split())
11
operations = []
12
​
13
for _ in range(m):
14
    operations.append(list(map(int, input().split())))
15
result = solve(n, operations)
16
print(result)
