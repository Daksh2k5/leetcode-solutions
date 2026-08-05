# Last updated: 8/5/2026, 12:04:31 PM
1from collections import Counter
2class Solution:
3    def containsDuplicate(self, nums: List[int]) -> bool:
4        c=Counter(nums).most_common()
5        if c[0][1]>1:
6            return True
7        return False