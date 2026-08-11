# Last updated: 8/11/2026, 9:12:42 AM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        count=nums[0]
4        for i in range(1,len(nums)):
5            if nums[i]-1==nums[i-1]:
6                count+=nums[i]
7            else:
8                break
9        while True:
10            if count in nums:
11                count+=1
12            else:
13                return count