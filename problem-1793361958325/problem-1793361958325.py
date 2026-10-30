# Last updated: 10/30/2026, 5:35:58 PM
1class Solution:
2    def rob(self, nums: list[int]) -> int:
3        if not nums:
4            return 0
5        if len(nums) < 3:
6            return max(nums)
7        p2 = nums[0]
8        p1 = max(nums[0], nums[1])
9        for n in nums[2:]:
10            curr = max(p1, p2 + n)
11            p2 = p1
12            p1 = curr
13        return p1