# Last updated: 8/4/2026, 1:14:44 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        res=max(nums)
4        cmin=cmax=1
5        for i in nums:
6            t=i*cmax
7            cmax=max(i*cmin,i*cmax,i)
8            cmin=min(i*cmin,t,i)
9            res=max(res,cmin,cmax)
10        return res