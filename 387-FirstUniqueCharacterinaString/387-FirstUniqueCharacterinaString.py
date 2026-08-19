# Last updated: 8/19/2026, 9:11:26 PM
1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        c=dict(Counter(s))
4        for i in range(len(s)):
5            if c[s[i]]==1:
6                return i 
7        return -1