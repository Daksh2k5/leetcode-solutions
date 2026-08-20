# Last updated: 8/20/2026, 10:47:07 AM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        arr1=[nums[0]]
4        arr2=[nums[1]]
5        nums=nums[2:]
6        for i in nums:
7            if arr1[-1]>arr2[-1]:
8                arr1.append(i)
9            else:
10                arr2.append(i)
11        return arr1+arr2