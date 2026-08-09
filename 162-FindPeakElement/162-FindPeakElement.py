# Last updated: 8/9/2026, 12:37:04 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)
        mid=(right+left)//2
        while True:
            mid=(right+left)//2
            if mid==0:
                if len(nums)==1:
                    return 0
                if nums[mid+1]<nums[mid]:
                    return mid
            if mid==len(nums)-1:
                if len(nums)==2:
                    return nums.index(max(nums))
                if nums[mid-1]<nums[mid]:
                    return mid
            print(mid,nums[mid])
            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            if nums[mid-1]>nums[mid+1]:
                right=mid
            else:
                left=mid