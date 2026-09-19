# Last updated: 9/17/2026, 7:04:26 AM
class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            a=0
            for i in str(num):
                a+=int(i)
            num=a
            if len(str(num))==1:
                return num