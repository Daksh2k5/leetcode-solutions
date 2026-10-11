# Last updated: 10/11/2026, 10:47:42 PM
1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        total = n * (n + 1) // 2
4        x = int(total ** 0.5)
5        if x * x == total:
6            return x
7        return -1