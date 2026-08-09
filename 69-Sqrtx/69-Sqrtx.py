# Last updated: 8/9/2026, 12:37:26 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1:
            return 1
        left=0
        right = x//2
        while left <= right:
            mid =(left +right)//2
            if (mid * mid) <= x and ((mid+1)*(mid+1))>x:
                return mid
            if (mid*mid)< x:
                left=mid+1
            else:
                right= mid-1