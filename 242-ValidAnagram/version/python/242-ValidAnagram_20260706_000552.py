# Last updated: 7/6/2026, 12:13:30 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
