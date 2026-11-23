# Last updated: 11/23/2026, 10:52:58 PM
1class Solution:
2    def sumOfMultiples(self, n: int) -> int:
3        ans=0
4        for i in range(1,n+1):
5            if i % 3 ==0 or i % 5 ==0 or i % 7 ==0:
6                ans+=i
7        return ans