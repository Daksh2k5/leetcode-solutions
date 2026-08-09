# Last updated: 8/9/2026, 12:36:53 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
