# Last updated: 8/19/2026, 9:11:26 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=dict(Counter(s))
        for i in range(len(s)):
            if c[s[i]]==1:
                return i 
        return -1