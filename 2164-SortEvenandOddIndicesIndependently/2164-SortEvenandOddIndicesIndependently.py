# Last updated: 10/2/2026, 1:50:35 PM
1class Solution:
2    def sortEvenOdd(self, nums: list[int]) -> list[int]:
3        l1=[]
4        l2=[]
5        ans=[]
6        for i in range(len(nums)):
7            if i%2!=0:
8                l1.append(nums[i])
9            else:
10                l2.append(nums[i])
11        l1.sort()
12        l2.sort()
13        l1=l1[::-1]
14        for i in range(len(nums)//2):
15            ans.append(l2[i])
16            ans.append(l1[i])
17        if len(nums)%2!=0:
18            ans.append(l2[-1])
19        return ans