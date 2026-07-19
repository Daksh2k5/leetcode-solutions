# Last updated: 7/19/2026, 5:20:35 PM
# i love python
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s=s.strip().split()
4        return len(s[-1])