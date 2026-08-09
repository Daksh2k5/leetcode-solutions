# Last updated: 8/9/2026, 12:37:58 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        for i in range(len(nums)):
            nums.pop()
        for i in s:
            nums.append(i)
        return (len(nums))