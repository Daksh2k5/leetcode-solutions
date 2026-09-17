# Last updated: 9/17/2026, 7:15:09 AM
1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n==0:
4            return False
5        while True:
6            if n%2==0:
7                n=n//2
8                continue
9            if n%3==0:
10                n=n//3
11                continue
12            if n%5==0:
13                n=n//5
14                continue
15            if n==1:
16                return True
17            return False