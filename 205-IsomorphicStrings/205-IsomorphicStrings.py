# Last updated: 8/28/2026, 11:43:45 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(x) for x in s] == [t.find(x) for x in t]