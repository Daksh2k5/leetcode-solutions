# Last updated: 7/18/2026, 1:05:09 PM
1from math import gcd
2class Solution:
3    def findGCD(self, nums: List[int]) -> int:
4        return gcd(min(nums),max(nums))