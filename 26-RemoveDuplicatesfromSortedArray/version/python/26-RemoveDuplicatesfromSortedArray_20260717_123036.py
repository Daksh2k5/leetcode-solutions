# Last updated: 7/17/2026, 12:30:36 PM
# i can do better
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        d={}
4        for i in nums:
5            d[i]=d.get(i,0)+1
6        for i in range(len(nums)):
7            nums.pop()
8        s=(list(d.keys()))
9        for i in s:
10            nums.append(i)
11        return len(nums)