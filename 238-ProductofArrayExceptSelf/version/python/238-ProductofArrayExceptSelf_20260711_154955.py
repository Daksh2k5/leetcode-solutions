# Last updated: 7/11/2026, 3:49:55 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if needle in haystack:
4            return haystack.index(needle)
5        else:
6            return -1