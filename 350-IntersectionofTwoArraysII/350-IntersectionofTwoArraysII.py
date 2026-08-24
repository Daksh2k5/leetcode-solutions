# Last updated: 8/24/2026, 11:03:52 PM
1from collections import Counter
2class Solution:
3    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
4        ans=[]
5        numsmin=min(nums1,nums2)
6        numsmax=max(nums1,nums2)
7        c=Counter(numsmin)
8        for i in numsmax:
9            if i in c:
10                if c[i]>0:
11                    ans.append(i)
12                    c[i]-=1
13        return ans