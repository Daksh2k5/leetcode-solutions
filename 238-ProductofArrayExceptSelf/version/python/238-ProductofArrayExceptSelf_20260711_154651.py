# Last updated: 7/11/2026, 3:46:51 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        for i in nums:
4            if i == 0:
5                nums.remove(i)
6                nums.append(0)
7        return nums    