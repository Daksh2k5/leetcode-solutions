# Last updated: 9/1/2026, 2:23:45 PM
1class Solution:
2    def maxDistinct(self, s: str) -> int:
3        return len(Counter(s))