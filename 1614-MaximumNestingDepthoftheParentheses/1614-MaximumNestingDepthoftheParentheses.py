# Last updated: 9/28/2026, 6:58:30 PM
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        maxi=0
4        c=0
5        for i in s:
6            if i == "(":
7                c+=1
8                maxi=max(c,maxi)
9            if i == ")":
10                c-=1
11        return maxi