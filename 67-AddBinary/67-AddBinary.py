# Last updated: 8/9/2026, 12:37:29 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]