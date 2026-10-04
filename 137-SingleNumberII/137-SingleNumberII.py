# Last updated: 10/4/2026, 5:29:24 PM
1class Solution:
2    def singleNumber(self, nums: list[int]) -> int:
3        c=Counter(nums)
4        for i in nums:
5            if c[i]==1:
6                return i