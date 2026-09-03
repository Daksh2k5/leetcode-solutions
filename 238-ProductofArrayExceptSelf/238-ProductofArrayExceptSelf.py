# Last updated: 8/26/2026, 11:08:34 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        if 0 in nums:
            nz=nums.copy()
            nz.remove(0)
            nzero=math.prod(nz)
        product=math.prod(nums)
        
        for i in nums:
            if i!=0:
                ans.append(product//i)
            else:
                ans.append(nzero)
        return(ans)