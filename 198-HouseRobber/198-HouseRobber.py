# Last updated: 10/16/2026, 12:55:07 PM
1#neetcode soln
2class Solution:
3    def rob(self, nums: list[int]) -> int:
4        if not nums:
5            return 0
6        if len(nums) < 3:
7            return max(nums)
8
9        p2 = nums[0]
10        p1 = max(nums[0], nums[1])
11
12        for n in nums[2:]:
13            curr = max(p1, p2 + n)
14            p2 = p1
15            p1 = curr
16
17        return p1