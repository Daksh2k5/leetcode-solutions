# Last updated: 8/18/2026, 10:16:03 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(set(nums))
        print(nums)
        count=1
        mlen=0
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
                mlen=max(mlen,count)
            else:
                count=1

        return mlen if mlen!=0 else 1
