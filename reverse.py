Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
Sample Input 1

2341
Sample Output 1

1432
 
1
?
2
if __name__ == '__main__':
3
    N=int(input())
4
    num = N
5
    reverse = 0
6
    while N != 0:
7
?
8
        digit = N % 10
9
        reverse = reverse * 10 + digit
10
        N = N // 10
11
    print(reverse)
