# Last updated: 9/7/2026, 9:14:54 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for i in nums:
            ans[i]=(nums[nums[i]])
        return ans