# Last updated: 8/25/2026, 9:08:23 AM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        step=k
        while True:
            if k in nums:
                k+=step
            else:
                return k