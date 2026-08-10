# Last updated: 8/9/2026, 12:35:33 PM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            nums[nums.index(min(nums))]*=multiplier
        return nums