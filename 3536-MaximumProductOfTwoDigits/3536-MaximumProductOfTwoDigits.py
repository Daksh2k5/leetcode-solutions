# Last updated: 8/9/2026, 12:35:21 PM
class Solution:
    def maxProduct(self, n: int) -> int:
        return sorted(int(x) for x in str(n))[-1]*sorted(int(x) for x in str(n))[-2]