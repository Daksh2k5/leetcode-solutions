# Last updated: 11/2/2026, 11:01:53 PM
1class Solution:
2    def minMoves2(self, nums: list[int]) -> int:
3        nums.sort()
4        m = nums[len(nums)//2]
5        return sum(abs(i-m) for i in nums)