# Last updated: 8/9/2026, 12:35:32 PM
from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s=prod([int(x) for x in str(n)])
            return n if s%t==0 else self.smallestNumber(n+1,t)