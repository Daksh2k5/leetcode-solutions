# Last updated: 10/2/2026, 1:35:19 PM
1class Solution:
2    def sortArrayByParity(self, nums: list[int]) -> list[int]:
3        o=[]
4        e=[]
5        for i in nums:
6            if i%2==0:
7                e.append(i)
8            else:
9                o.append(i)
10        return e + o