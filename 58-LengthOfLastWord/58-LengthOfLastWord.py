# Last updated: 8/9/2026, 12:37:33 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split()
        return len(s[-1])