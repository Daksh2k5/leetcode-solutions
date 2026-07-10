# Last updated: 7/10/2026, 9:41:59 PM
'''
proud of the runtime
topcoder
'''

1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        count=0
4        for i in range(len(nums)):
5            if nums[i] == val:
6                nums[i]=101
7            else:
8                count+=1
9        nums.sort()
10        return count  
11