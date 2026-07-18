# Last updated: 7/18/2026, 12:51:40 PM
1from math import gcd
2class Solution:
3    def findGCD(self, nums: List[int]) -> int:
4        nums.sort()
5        return gcd(nums[0],nums[-1])