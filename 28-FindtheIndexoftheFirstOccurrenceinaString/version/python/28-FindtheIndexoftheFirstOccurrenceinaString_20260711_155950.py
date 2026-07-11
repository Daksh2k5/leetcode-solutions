# Last updated: 7/11/2026, 3:59:50 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        try:
4            return haystack.index(needle)
5        except ValueError:
6            return -1