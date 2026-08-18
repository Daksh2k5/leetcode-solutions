# Last updated: 8/18/2026, 1:03:05 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n == 1 or n == 2 :
4            return n 
5        a = 1
6        b = 2
7        for i in range(3,n+1):
8            c = a + b
9            a = b
10            b = c
11        return c