# Last updated: 8/23/2026, 4:34:52 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        return [s.find(c) for c in s] == [t.find(c) for c in t]