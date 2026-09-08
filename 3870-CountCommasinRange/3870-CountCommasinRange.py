# Last updated: 9/8/2026, 8:22:57 PM
class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)