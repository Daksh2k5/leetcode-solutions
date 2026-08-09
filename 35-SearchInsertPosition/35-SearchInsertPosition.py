# Last updated: 8/9/2026, 12:37:47 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target<min(nums):
            return 0
        if target>max(nums):
            return len(nums)
        for i in range(len(nums)-1):
            if target==nums[i]:
                return i
            if target>nums[i] and target<nums[i+1]:
                return int(i)+1