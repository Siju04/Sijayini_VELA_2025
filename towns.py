Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city  is the starting location. The number of roads from city  to city  is the first value in the array, from city  to city  is the second, and so on.

How many paths are there from city  to the last city in the list, modulo ?

Example


There are  roads to city ,  roads to city  and  roads to city . The total number of roads is .

Note
Pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn.

Function Description

Complete the connectingTowns function in the editor below.

connectingTowns has the following parameters:

int n: the number of towns
int routes[n-1]: the number of routes between towns
Returns

int: the total number of routes, modulo 1234567.
Input Format
The first line contains an integer T, T test-cases follow.

Each test-case has 2 lines.
The first line contains an integer N (the number of towns).
The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1

Constraints
1 <= T<=1000
2< N <=100
1 <= routes[i] <=1000

Sample Input

2
3
1 3
4
2 2 2
Sample Output

3
8
Explanation
Case 1: 1 route from T1 to T2, 3 routes from T2 to T3, hence only 3 routes.
Case 2: There are 2 routes from each city to the next, hence 2 * 2 * 2 = 8.
1
def connectingTowns(n, routes):
2
    total_routes = 1
3
    for route in routes:
4
        total_routes = (total_routes * route) % 1234567
5
    return total_routes
6
t = int(input())
7
for _ in range(t):
8
    n = int(input())
9
    routes = list(map(int, input().split()))
10
    result = connectingTowns(n, routes)
11
    print(result)
