Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1
Explanation

Test Case #01: We split  into two strings ='aaa' and ='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams.

Test Case #02: You have to replace 'a' with 'b', which will generate "bb".

Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another.

Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one.

Test Case #05:  and  are already anagrams of one another.

Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".
 
1
def anagram(s):
2
    n = len(s)
3
    if n % 2 != 0:
4
        return -1
5
    
6
    s1 = s[:n // 2]
7
    s2 = s[n // 2:]
8
    freq_s1 = {}
9
    freq_s2 = {}
10
    for char in s1:
11
        freq_s1[char] = freq_s1.get(char, 0) + 1
12
    for char in s2:
13
        freq_s2[char] = freq_s2.get(char, 0) + 1
14
    min_changes = 0
15
    for char, freq in freq_s2.items():
16
        if char not in freq_s1:
17
            min_changes += freq
18
        else:
19
            min_changes += max(freq - freq_s1[char], 0)
20
    
21
    return min_changes
22
t = int(input())
23
for _ in range(t):
24
    s = input()
25
    result = anagram(s)
26
    print(result)
27
​
