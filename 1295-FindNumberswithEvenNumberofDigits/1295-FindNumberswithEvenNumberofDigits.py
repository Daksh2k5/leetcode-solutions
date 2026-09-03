# Last updated: 8/18/2026, 9:07:52 AM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count