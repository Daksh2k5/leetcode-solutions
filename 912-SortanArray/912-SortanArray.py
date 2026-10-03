# Last updated: 10/3/2026, 10:44:56 AM
1class Solution:
2    def sortArray(self, nums: list[int]) -> list[int]:
3        if len(nums)<=1:
4            return nums
5        pivot=nums[random.randint(0,len(nums)-1)]
6        s=[]
7        m=[]
8        b=[]
9        for i in nums:
10            if i<pivot:
11                s.append(i)
12            if i==pivot:
13                m.append(i)
14            if i>pivot:
15                b.append(i)
16        return self.sortArray(s)+m+self.sortArray(b)