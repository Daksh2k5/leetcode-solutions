# Last updated: 9/24/2026, 6:44:22 PM
1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            sum=0
5            for j in str(nums[i]):
6                sum+=int(j)
7            if sum==i:
8                return i
9        return -1