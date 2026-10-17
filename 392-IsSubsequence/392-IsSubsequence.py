# Last updated: 10/17/2026, 2:23:10 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i = 0
4        for c in t:
5            if i < len(s) and s[i] == c:
6                i += 1
7        return i == len(s)