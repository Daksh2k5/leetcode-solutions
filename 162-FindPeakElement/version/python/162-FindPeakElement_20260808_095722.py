# Last updated: 8/8/2026, 9:57:22 AM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        left=0
4        right=len(nums)
5        mid=(right+left)//2
6        while True:
7            mid=(right+left)//2
8            if mid==0:
9                if len(nums)==1:
10                    return 0
11                if nums[mid+1]<nums[mid]:
12                    return mid
13            if mid==len(nums)-1:
14                if len(nums)==2:
15                    return nums.index(max(nums))
16                if nums[mid-1]<nums[mid]:
17                    return mid
18            print(mid,nums[mid])
19            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
20                return mid
21            if nums[mid-1]>nums[mid+1]:
22                right=mid
23            else:
24                left=mid