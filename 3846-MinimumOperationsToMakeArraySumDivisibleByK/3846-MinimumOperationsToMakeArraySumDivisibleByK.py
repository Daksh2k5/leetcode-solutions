# Last updated: 8/10/2026, 10:21:08 AM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (sum(nums)%k)