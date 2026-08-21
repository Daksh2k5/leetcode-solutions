# Last updated: 8/21/2026, 3:42:49 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        return int(f"{n:032b}"[::-1],2)