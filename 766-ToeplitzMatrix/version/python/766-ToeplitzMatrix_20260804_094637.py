# Last updated: 8/4/2026, 9:46:37 AM
# Kadane's Algorithm
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        s=0
4        maxi=nums[0]
5        for i in nums:
6            s+=i
7            maxi=max(maxi,s)
8            print(i,"s=",s,"maxi=",maxi)
9            if s < 0:
10                s=0
11        return maxi