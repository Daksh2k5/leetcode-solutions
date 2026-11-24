# Last updated: 11/24/2026, 10:55:06 PM
1from math import gcd, lcm
2class Solution:
3    def maxLength(self, nums: list[int]) -> int:
4        length = len(nums)
5        ans = 0
6        max_possible = lcm(*nums) * max(nums)
7        for left in range(length):
8            current_prod = 1
9            current_lcm = 1
10            current_gcd = 0
11            for right in range(left, length):
12                val = nums[right]
13                current_prod *= val
14                current_lcm = lcm(current_lcm, val)
15                current_gcd = gcd(current_gcd, val)
16                if current_prod == current_lcm * current_gcd:
17                    ans = max(ans, right - left + 1)
18
19                if current_prod > max_possible:
20                    break
21
22        return ans