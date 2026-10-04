# Last updated: 10/4/2026, 5:31:27 PM
1class Solution:
2    def singleNumber(self, nums: list[int]) -> list[int]:
3        c=Counter(nums)
4        ans=[]
5        for i in c:
6            if c[i]==1:
7                ans.append(i)
8        return ans