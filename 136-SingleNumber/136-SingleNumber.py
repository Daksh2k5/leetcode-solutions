# Last updated: 8/9/2026, 12:37:12 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==1:
                return i