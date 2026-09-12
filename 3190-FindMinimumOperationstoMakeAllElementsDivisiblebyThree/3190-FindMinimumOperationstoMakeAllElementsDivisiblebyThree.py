# Last updated: 9/12/2026, 5:51:22 PM
1class Solution:
2    def minimumOperations(self, nums: List[int]) -> int:
3        count=0
4        for i in nums:
5            if i%3!=0:
6                count+=1
7        return count