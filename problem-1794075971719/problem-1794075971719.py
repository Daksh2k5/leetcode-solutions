# Last updated: 11/7/2026, 11:56:11 PM
1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        if n==1:
4            return 2
5        if n % 2 == 0:
6            return n
7        while n % 2 != 0:
8            n += n
9        return n