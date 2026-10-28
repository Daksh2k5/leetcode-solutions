# Last updated: 10/28/2026, 9:49:08 AM
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3            for i , j in enumerate(nums):
4                if j==target:
5                    return i
6            return -1