# Last updated: 8/9/2026, 12:35:46 PM
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums),max(nums))