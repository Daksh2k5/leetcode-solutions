# Last updated: 9/9/2026, 11:24:28 PM
1class Solution:
2    def concatWithReverse(self, nums: list[int]) -> list[int]:
3        return nums+nums[::-1]