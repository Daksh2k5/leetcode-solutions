# Last updated: 8/8/2026, 9:05:31 AM
1from collections import Counter
2class Solution:
3    def findContentChildren(self, g: List[int], s: List[int]) -> int:
4        count = 0
5        i = 0
6        j = 0
7        g = sorted(g)
8        s = sorted(s)
9        while i < len(g) and j < len(s):
10            if s[j] >= g[i]:
11                count += 1
12                i += 1
13                j += 1
14            else:
15                j += 1
16        return count