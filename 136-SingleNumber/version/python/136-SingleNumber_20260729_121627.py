# Last updated: 7/29/2026, 12:16:27 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        d={}
4        for i in nums:
5            d[i]=d.get(i,0)+1
6        for i in d:
7            if d[i]==1:
8                return i