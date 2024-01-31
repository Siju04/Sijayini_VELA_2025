Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
 
1
def digit_sum(num):
2
    return sum(int(digit) for digit in str(num))
3
​
4
def best_divisor(n):
5
    best_div = 1
6
    max_digit_sum = 1
7
​
8
    for i in range(2, n + 1):
9
        if n % i == 0:
10
            current_digit_sum = digit_sum(i)
11
            if current_digit_sum > max_digit_sum or (current_digit_sum == max_digit_sum and i < best_div):
12
                best_div = i
13
                max_digit_sum = current_digit_sum
14
​
15
    return best_div
16
n = int(input())
17
result = best_divisor(n)
18
print(result)
