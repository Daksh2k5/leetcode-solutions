# Last updated: 8/18/2026, 9:00:41 AM
from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=Counter(nums)
        l=[]
        if k==1:
            for i in c:
                if c[i]==1:
                    l.append(i)
            try:
                return max(l)
            except ValueError:
                return -1
        if k==n:
            return max(nums)
        if k<n:
            if c[nums[0]]==1 and c[nums[-1]]!=1:
                return nums[0]
            if c[nums[0]]!=1 and c[nums[-1]]==1:
                return nums[-1]
            if c[nums[0]]==1 and c[nums[-1]]==1:
                return max(nums[0],nums[-1])
            if c[nums[0]]!=1 and c[nums[-1]]!=1:
                return -1