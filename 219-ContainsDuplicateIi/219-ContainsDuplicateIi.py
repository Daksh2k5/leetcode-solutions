# Last updated: 8/9/2026, 12:36:49 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in range(len(nums)):
            if d[nums[i]]>1:
                for j in range(i+1,len(nums)):
                    if nums[j]==nums[i] and abs(i-j)<=k:
                        return True
        return False