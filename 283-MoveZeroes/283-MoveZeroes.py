# Last updated: 8/9/2026, 12:36:42 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums    