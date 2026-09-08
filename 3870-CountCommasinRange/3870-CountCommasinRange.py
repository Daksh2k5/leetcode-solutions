# Last updated: 9/8/2026, 8:22:29 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        if n>999:
4            return n-999
5        return 0                