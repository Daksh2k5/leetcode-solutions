# Last updated: 8/9/2026, 12:37:01 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]