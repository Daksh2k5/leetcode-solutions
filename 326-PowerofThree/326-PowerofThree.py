# Last updated: 8/13/2026, 12:09:38 PM
1class Solution:
2    def isPowerOfThree(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        return n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3))