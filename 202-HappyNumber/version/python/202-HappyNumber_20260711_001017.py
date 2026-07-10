# Last updated: 7/11/2026, 12:10:17 AM
# beat this.
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        num=n
4        while num!=4:
5            temp=0
6            for i in str(num):
7                temp=temp+(int(i)**2)
8            num=int(temp)
9            if num==1:
10                return True
11        return False
12        