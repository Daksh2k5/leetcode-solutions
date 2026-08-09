# Last updated: 8/9/2026, 12:37:56 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i]=101
            else:
                count+=1
        nums.sort()
        return count  
