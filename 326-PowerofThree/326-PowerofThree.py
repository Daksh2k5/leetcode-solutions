# Last updated: 8/13/2026, 12:09:38 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3))