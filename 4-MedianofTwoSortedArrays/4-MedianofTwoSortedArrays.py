# Last updated: 8/15/2026, 10:43:45 AM
1from statistics import median
2class Solution:
3    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
4        return median(nums1+nums2)