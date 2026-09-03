# Last updated: 8/15/2026, 10:43:45 AM
from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1+nums2)