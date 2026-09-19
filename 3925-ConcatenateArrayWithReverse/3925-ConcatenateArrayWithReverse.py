# Last updated: 9/9/2026, 11:25:30 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]