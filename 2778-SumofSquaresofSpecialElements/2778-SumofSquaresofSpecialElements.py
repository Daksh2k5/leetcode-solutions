# Last updated: 10/11/2026, 2:34:56 PM
1class Solution:
2    def sumOfSquares(self, nums: List[int]) -> int:
3        ans=0
4        n=len(nums)
5        for i in range(1,n+1):
6            if n%i==0:
7                # print(i,nums[i-1])
8                ans+=nums[i-1]*nums[i-1]
9        return ans