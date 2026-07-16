# Last updated: 7/16/2026, 11:26:09 PM
1import math
2class Solution:
3    def gcdSum(self, nums: list[int]) -> int:
4        mx=nums[0]
5        l=[]
6        GCD=[]
7        sum=0
8        for i in range(len(nums)):
9            if nums[i]>mx:
10                mx=nums[i]
11                l.append(nums[i])
12            else:
13                l.append(mx)
14        for i in range((len(nums))):
15            GCD.append(gcd(nums[i],l[i]))
16        GCD.sort()
17        mx=0
18        for i in range(len(nums)//2):
19            mx+=gcd(GCD[0],GCD[-1])
20            GCD.pop(0)
21            GCD.pop(-1)
22        return mx