# Last updated: 8/9/2026, 12:36:25 PM
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = max3 = float("-inf")

        for x in nums:
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
        return (max(max1*max2*max3,min1*min2*max1))