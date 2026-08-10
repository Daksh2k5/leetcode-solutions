# Last updated: 8/10/2026, 10:01:46 AM
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        return (sum(nums)%k)