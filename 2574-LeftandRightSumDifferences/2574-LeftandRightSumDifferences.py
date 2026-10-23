# Last updated: 10/23/2026, 2:53:19 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        total_sum = sum(nums)
4        left_sum = 0
5        ans = []
6        for x in nums:
7            right_sum = total_sum - left_sum - x
8            ans.append(abs(left_sum - right_sum))
9            left_sum += x 
10        return ans