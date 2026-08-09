# Last updated: 8/9/2026, 12:37:22 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3=sorted(nums1[:m]+nums2[:n])
        nums1.clear()
        for i in range(m+n):
            nums1.append(nums3[i])