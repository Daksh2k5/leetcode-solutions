# Last updated: 7/25/2026, 3:05:34 PM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        return sorted(int(x) for x in str(n))[-1]*sorted(int(x) for x in str(n))[-2]