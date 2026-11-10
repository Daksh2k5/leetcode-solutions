# Last updated: 11/10/2026, 2:41:09 PM
1class Solution:
2    def separateDigits(self, nums: list[int]) -> list[int]:
3        ans=[]
4        for i in nums:
5            for j in str(i):
6                ans.append(int(j))
7
8        return ans