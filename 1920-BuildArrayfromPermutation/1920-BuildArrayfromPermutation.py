# Last updated: 9/7/2026, 9:14:54 PM
1class Solution:
2    def buildArray(self, nums: List[int]) -> List[int]:
3        ans=[0]*len(nums)
4        for i in nums:
5            ans[i]=(nums[nums[i]])
6        return ans