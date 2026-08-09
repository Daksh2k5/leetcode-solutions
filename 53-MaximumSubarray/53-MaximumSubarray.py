# Last updated: 8/9/2026, 12:37:40 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=maxi=nums[0]
        for i in nums[1:]:
            s=max(s,0)+i
            maxi=max(maxi,s)
        return maxi