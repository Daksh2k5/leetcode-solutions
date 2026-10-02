# Last updated: 10/2/2026, 1:40:43 PM
1class Solution:
2    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
3        o=[]
4        e=[]
5        ans=[]
6        for i in nums:
7            if i%2==0:
8                e.append(i)
9            else:
10                o.append(i)
11        for i in range(len(o)):
12            ans.append(e[i])
13            ans.append(o[i])
14        return ans