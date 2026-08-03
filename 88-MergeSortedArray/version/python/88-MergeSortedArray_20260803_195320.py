# Last updated: 8/3/2026, 7:53:20 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        nums3=sorted(nums1[:m]+nums2[:n])
4        nums1.clear()
5        for i in range(m+n):
6            nums1.append(nums3[i])