# Last updated: 8/12/2026, 6:42:02 PM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        return n > 0 and (n & (n - 1)) == 0
4