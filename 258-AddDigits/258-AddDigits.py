# Last updated: 9/17/2026, 7:04:26 AM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        while True:
4            a=0
5            for i in str(num):
6                a+=int(i)
7            num=a
8            if len(str(num))==1:
9                return num