# Last updated: 7/5/2026, 8:19:26 PM
# not optimal
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums.sort()
4        for i in range(1,len(nums)):
5            if nums[i]==nums[i-1]:
6                return True
7        return False