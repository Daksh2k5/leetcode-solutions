# Last updated: 8/22/2026, 10:43:21 AM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        s=0
4        p=1
5        for i in str(n):
6            s+=int(i)
7            p*=int(i)
8        return n%(s+p)==0