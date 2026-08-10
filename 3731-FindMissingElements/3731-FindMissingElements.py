# Last updated: 8/9/2026, 12:35:19 PM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=[x for x in range(min(nums),max(nums)+1)]
        return [x for x in n if x not in nums]