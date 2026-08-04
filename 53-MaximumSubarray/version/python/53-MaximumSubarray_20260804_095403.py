# Last updated: 8/4/2026, 9:54:03 AM
# Kadane's Algorithm
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        s=maxi=nums[0]
4        for i in nums[1:]:
5            s=max(s,0)+i
6            maxi=max(maxi,s)
7        return maxi