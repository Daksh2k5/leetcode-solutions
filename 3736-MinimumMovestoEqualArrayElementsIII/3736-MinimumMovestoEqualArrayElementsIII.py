# Last updated: 11/3/2026, 9:44:37 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        return max(nums)*len(nums)-sum(nums)