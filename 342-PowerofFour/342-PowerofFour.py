# Last updated: 8/16/2026, 10:46:14 AM
1class Solution:
2    def isPowerOfFour(self, n: int) -> bool:
3        return n > 0 and (n & (n - 1)) == 0 and (n % 3 == 1)    