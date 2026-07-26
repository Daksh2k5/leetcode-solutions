# Last updated: 7/26/2026, 1:46:56 PM
'''
runtime- 16ms (73.57*)
memory -20.24MB (78.13*)
'''

1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums=sorted(nums)
4        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])