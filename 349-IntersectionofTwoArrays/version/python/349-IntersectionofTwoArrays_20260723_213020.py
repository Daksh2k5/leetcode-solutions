# Last updated: 7/23/2026, 9:30:20 PM
'''
runtime-0ms (100%*)
memory-19.3MB (80.67&*)
no biggie
'''

1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        return list(set(nums1)&set(nums2))  