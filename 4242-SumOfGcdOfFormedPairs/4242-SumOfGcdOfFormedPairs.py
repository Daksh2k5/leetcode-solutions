# Last updated: 8/9/2026, 12:35:22 PM
import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=nums[0]
        l=[]
        GCD=[]
        sum=0
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
                l.append(nums[i])
            else:
                l.append(mx)
        for i in range((len(nums))):
            GCD.append(gcd(nums[i],l[i]))
        GCD.sort()
        mx=0
        for i in range(len(nums)//2):
            mx+=gcd(GCD[0],GCD[-1])
            GCD.pop(0)
            GCD.pop(-1)
        return mx