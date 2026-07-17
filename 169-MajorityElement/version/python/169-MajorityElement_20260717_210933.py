# Last updated: 7/17/2026, 9:09:33 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        count=0
4        j=nums[0]
5        for i in nums:
6            if j == i:
7                count+=1
8            else:
9                count-=1
10            if count <1:
11                count=1
12                j=i
13        return j