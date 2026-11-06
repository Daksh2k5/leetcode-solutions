# Last updated: 11/6/2026, 4:04:06 PM
1class Solution:
2    def alternatingSum(self, nums: List[int]) -> int:
3        ans=0
4        for i in range(len(nums)):
5            if i%2==0:
6                ans+=nums[i]
7            else:
8                ans-=nums[i]
9        return ans