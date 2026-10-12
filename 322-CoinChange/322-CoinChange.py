# Last updated: 10/12/2026, 8:41:49 PM
# from functools import reduce
from math import gcd

class Solution:
    def coinChange(self, C, T):
        if T == 0:
            return 0

        C = list(set(c for c in C if c <= T))

        if not C:
            return -1

        if len(C) == 1:
            return T // C[0] if T % C[0] == 0 else -1

        g = reduce(gcd, C)

        if T % g:
            return -1

        # Shrink the entire problem when all values
        # share a common divisor
        if g > 1:
            T //= g
            C = [c // g for c in C]

        reach = 1
        seen = 1
        step = 0

        mask = (1 << (T + 1)) - 1
        target_bit = 1 << T

        while reach:
            step += 1
            nxt = 0

            for c in C:
                nxt |= reach << c

            # Remove amounts above the target
            nxt &= mask

            # Only keep amounts not reached at an earlier depth
            nxt &= ~seen

            if nxt & target_bit:
                return step

            if not nxt:
                return -1

            seen |= nxt
            reach = nxt

        return -1