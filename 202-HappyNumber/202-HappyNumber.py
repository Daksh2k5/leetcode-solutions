# Last updated: 8/9/2026, 12:36:55 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        num=n
        while num!=4:
            temp=0
            for i in str(num):
                temp=temp+(int(i)**2)
            num=int(temp)
            if num==1:
                return True
        return False
        