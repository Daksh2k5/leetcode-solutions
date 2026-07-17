# Last updated: 7/17/2026, 9:29:42 PM
# I love one line answers
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        return bin(int(a,2)+int(b,2))[2:]