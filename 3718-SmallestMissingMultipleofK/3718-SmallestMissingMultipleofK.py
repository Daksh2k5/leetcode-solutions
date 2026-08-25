# Last updated: 8/25/2026, 9:08:23 AM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        nums=set(nums)
4        step=k
5        while True:
6            if k in nums:
7                k+=step
8            else:
9                return k