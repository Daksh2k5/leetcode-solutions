# Last updated: 8/9/2026, 12:36:36 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))  