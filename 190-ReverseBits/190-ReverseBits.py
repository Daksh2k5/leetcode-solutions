# Last updated: 8/21/2026, 3:42:58 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1],2)