# Last updated: 8/18/2026, 9:07:52 AM
1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        count=0
4        for i in nums:
5            if len(str(i))%2==0:
6                count+=1
7        return count