# Last updated: 8/9/2026, 12:36:46 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s))==sorted(list(t))