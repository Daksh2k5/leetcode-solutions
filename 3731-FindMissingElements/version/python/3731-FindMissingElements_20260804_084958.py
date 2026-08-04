# Last updated: 8/4/2026, 8:49:58 AM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        n=[x for x in range(min(nums),max(nums)+1)]
4        return [x for x in n if x not in nums]