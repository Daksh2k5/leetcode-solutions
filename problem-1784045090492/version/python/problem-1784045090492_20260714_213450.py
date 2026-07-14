# Last updated: 7/14/2026, 9:34:50 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        ans = [-1] * len(nums1)
4
5        for i in range(len(nums1)):
6            current_val = nums1[i]
7            idx = nums2.index(current_val)
8
9            for j in range(idx + 1, len(nums2)):
10                if nums2[j] > current_val:
11                    ans[i] = nums2[j]
12                    break
13
14        return ans
15