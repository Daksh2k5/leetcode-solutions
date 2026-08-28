# Last updated: 8/28/2026, 11:43:45 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        return [s.find(x) for x in s] == [t.find(x) for x in t]