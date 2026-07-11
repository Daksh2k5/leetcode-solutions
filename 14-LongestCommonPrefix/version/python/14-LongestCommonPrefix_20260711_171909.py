# Last updated: 7/11/2026, 5:19:09 PM
# i overcomplicated it when i solved it the first time
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return ""
5        strs.sort()
6        first, last = strs[0], strs[-1]
7        i = 0
8        while i < len(first) and i < len(last) and first[i] == last[i]:
9            i += 1
10        return first[:i]
11