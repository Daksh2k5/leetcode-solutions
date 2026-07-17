# Last updated: 7/17/2026, 9:18:25 PM
# excellent runtime
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        nums.sort()
4        return nums[len(nums)//2]