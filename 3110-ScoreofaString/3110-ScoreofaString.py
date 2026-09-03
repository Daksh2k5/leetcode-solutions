# Last updated: 9/3/2026, 9:31:38 AM
class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        for i in range(len(s)-1):
            score+= abs(ord(s[i])-ord(s[i+1]))
        return score