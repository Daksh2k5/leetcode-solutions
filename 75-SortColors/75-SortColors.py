# Last updated: 8/17/2026, 6:12:25 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        for i in range(len(nums),0,-1):
4            x=nums.pop(nums.index(min(nums[:i])))
5            nums.append(x)