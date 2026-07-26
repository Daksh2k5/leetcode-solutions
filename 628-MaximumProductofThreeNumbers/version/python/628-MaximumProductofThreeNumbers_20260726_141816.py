# Last updated: 7/26/2026, 2:18:16 PM
'''
Rutime- 10ms (87.89%*)
Memory- 20.48 (17.11%)
'''

1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        min1 = min2 = float("inf")
4        max1 = max2 = max3 = float("-inf")
5
6        for x in nums:
7            if x < min1:
8                min1, min2 = x, min1
9            elif x < min2:
10                min2 = x
11            if x > max1:
12                max1, max2, max3 = x, max1, max2
13            elif x > max2:
14                max2, max3 = x, max2
15            elif x > max3:
16                max3 = x
17        return (max(max1*max2*max3,min1*min2*max1))