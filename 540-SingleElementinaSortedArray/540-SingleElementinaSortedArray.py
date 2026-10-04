# Last updated: 10/4/2026, 5:34:09 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        c=Counter(nums)
4        for i in c:
5            if c[i]==1:
6                return i