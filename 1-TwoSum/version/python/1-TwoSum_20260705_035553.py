# Last updated: 7/5/2026, 3:55:53 AM
# brute force
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for i in range(len(nums)):
4            for j in range(i,len(nums)):
5                if nums[i]+nums[j]==target and i!=j:
6                    return[i,j]