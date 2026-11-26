# Last updated: 11/26/2026, 12:48:18 PM
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        for i in range(10,0,-1):
4            n=n-i
5            if n<0:
6                return i%2!=0
7        return i%2==0