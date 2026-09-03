# Last updated: 8/11/2026, 9:12:42 AM
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        count=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                count+=nums[i]
            else:
                break
        while True:
            if count in nums:
                count+=1
            else:
                return count