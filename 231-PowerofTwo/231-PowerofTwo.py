# Last updated: 8/12/2026, 6:42:02 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
