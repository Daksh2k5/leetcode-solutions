# Last updated: 11/20/2026, 1:42:45 PM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        return abs(int(str(n)[::-1])-n)