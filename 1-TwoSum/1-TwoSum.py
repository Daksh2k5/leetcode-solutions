# Last updated: 8/9/2026, 12:38:13 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if target-nums[i] in l:
                return [i,l.index(target-nums[i])]
            else:
                l.append(nums[i])
        return []
