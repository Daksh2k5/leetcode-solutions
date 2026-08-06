# Last updated: 8/6/2026, 8:58:37 AM
1from math import prod
2class Solution:
3    def smallestNumber(self, n: int, t: int) -> int:
4        while True:
5            s=prod([int(x) for x in str(n)])
6            return n if s%t==0 else self.smallestNumber(n+1,t)