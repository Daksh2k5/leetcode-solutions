# Last updated: 8/20/2026, 10:47:07 AM
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        nums=nums[2:]
        for i in nums:
            if arr1[-1]>arr2[-1]:
                arr1.append(i)
            else:
                arr2.append(i)
        return arr1+arr2