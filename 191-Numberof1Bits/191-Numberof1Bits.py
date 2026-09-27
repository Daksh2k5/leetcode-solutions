# Last updated: 9/22/2026, 9:47:24 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        count=1
4        while n >1:
5            if n%2!=0:
6                count+=1
7            n=n//2
8        return count