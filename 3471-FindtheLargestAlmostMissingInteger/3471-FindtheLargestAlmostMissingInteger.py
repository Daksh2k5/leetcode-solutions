# Last updated: 8/18/2026, 9:00:41 AM
1from collections import Counter
2class Solution:
3    def largestInteger(self, nums: List[int], k: int) -> int:
4        n=len(nums)
5        c=Counter(nums)
6        l=[]
7        if k==1:
8            for i in c:
9                if c[i]==1:
10                    l.append(i)
11            try:
12                return max(l)
13            except ValueError:
14                return -1
15        if k==n:
16            return max(nums)
17        if k<n:
18            if c[nums[0]]==1 and c[nums[-1]]!=1:
19                return nums[0]
20            if c[nums[0]]!=1 and c[nums[-1]]==1:
21                return nums[-1]
22            if c[nums[0]]==1 and c[nums[-1]]==1:
23                return max(nums[0],nums[-1])
24            if c[nums[0]]!=1 and c[nums[-1]]!=1:
25                return -1