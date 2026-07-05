# Last updated: 7/6/2026, 12:05:52 AM
# shorter code
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return sorted(list(s))==sorted(list(t))