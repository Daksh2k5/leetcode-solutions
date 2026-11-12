# Last updated: 11/12/2026, 11:33:46 AM
1class Solution:
2    def longestMonotonicSubarray(self, nums: list[int]) -> int:
3        n = len(nums)
4        ans = 1
5        for i in range(n):
6            for j in range(i + 1, n):
7                inc = True
8                dec = True
9                for k in range(i, j):
10                    if nums[k] >= nums[k + 1]:
11                        inc = False
12                    if nums[k] <= nums[k + 1]:
13                        dec = False
14                if inc or dec:
15                    ans = max(ans, j - i + 1)
16        return ans