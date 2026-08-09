# Last updated: 8/9/2026, 12:37:08 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cmin=cmax=1
        for i in nums:
            t=i*cmax
            cmax=max(i*cmin,i*cmax,i)
            cmin=min(i*cmin,t,i)
            res=max(res,cmin,cmax)
        return res