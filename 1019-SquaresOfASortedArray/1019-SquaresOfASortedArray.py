# Last updated: 8/9/2026, 12:36:05 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums]) 