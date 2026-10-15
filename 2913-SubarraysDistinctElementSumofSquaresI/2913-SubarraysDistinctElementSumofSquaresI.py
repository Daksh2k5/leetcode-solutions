# Last updated: 10/15/2026, 1:50:54 PM
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        ans = 0
4        for i in range(len(nums)):
5            uni = set()
6            for j in range(i, len(nums)):
7                uni.add(nums[j])
8                ans += len(uni) ** 2
9        return ans