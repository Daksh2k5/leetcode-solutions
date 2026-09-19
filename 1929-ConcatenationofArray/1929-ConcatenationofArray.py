# Last updated: 9/7/2026, 9:16:32 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums