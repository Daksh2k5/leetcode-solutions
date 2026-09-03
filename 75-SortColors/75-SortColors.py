# Last updated: 8/17/2026, 6:12:25 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums),0,-1):
            x=nums.pop(nums.index(min(nums[:i])))
            nums.append(x)