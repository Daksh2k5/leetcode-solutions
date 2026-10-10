# Last updated: 10/10/2026, 2:41:23 PM
1class Solution:
2    def thirdMax(self, nums: list[int]) -> int:
3        nums=sorted(set(nums))
4        if len(nums)<3:
5            return nums[-1]
6        else:
7            return nums[-3]