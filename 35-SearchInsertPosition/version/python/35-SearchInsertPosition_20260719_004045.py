# Last updated: 7/19/2026, 12:40:45 AM
# not proud of this one, will improve later
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        if target in nums:
4            return nums.index(target)
5        if target<min(nums):
6            return 0
7        if target>max(nums):
8            return len(nums)
9        for i in range(len(nums)-1):
10            if target==nums[i]:
11                return i
12            if target>nums[i] and target<nums[i+1]:
13                return int(i)+1