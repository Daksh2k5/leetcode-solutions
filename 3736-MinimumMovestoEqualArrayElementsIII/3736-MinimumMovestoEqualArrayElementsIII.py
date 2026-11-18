# Last updated: 11/18/2026, 3:52:34 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        return max(nums)*len(nums)-sum(nums)