# Last updated: 8/26/2026, 11:08:34 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        ans=[]
4        if 0 in nums:
5            nz=nums.copy()
6            nz.remove(0)
7            nzero=math.prod(nz)
8        product=math.prod(nums)
9        
10        for i in nums:
11            if i!=0:
12                ans.append(product//i)
13            else:
14                ans.append(nzero)
15        return(ans)