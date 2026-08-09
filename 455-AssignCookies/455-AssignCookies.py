# Last updated: 8/9/2026, 12:36:33 PM
from collections import Counter
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i = 0
        j = 0
        g = sorted(g)
        s = sorted(s)
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count