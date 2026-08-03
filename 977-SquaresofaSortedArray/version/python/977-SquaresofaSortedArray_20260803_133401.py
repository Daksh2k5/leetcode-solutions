# Last updated: 8/3/2026, 1:34:01 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        return sorted([x**2 for x in nums]) 