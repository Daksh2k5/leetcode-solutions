# Last updated: 11/22/2026, 1:09:59 AM
1class Solution:
2    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
3        res = []
4        for i in range(len(nums)):
5            count = 0
6            for j in range(len(nums)):
7                if nums[j] < nums[i]:
8                    count += 1
9            res.append(count)
10        return res            
11