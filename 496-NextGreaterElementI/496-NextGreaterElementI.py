# Last updated: 8/9/2026, 12:36:30 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        for i in range(len(nums1)):
            current_val = nums1[i]
            idx = nums2.index(current_val)

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > current_val:
                    ans[i] = nums2[j]
                    break

        return ans
