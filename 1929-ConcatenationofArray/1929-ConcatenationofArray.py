# Last updated: 9/7/2026, 9:16:32 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        nums.extend(nums)
4        return nums