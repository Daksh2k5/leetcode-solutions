# Last updated: 7/5/2026, 11:52:07 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s=list(s)
4        t=list(t)
5        s.sort()
6        t.sort()
7        return s==t 