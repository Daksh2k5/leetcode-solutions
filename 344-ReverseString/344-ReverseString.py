# Last updated: 9/30/2026, 2:40:55 PM
1class Solution:
2    def reverseString(self, s: list[str]) -> None:
3        a=s.copy()
4        a=a[::-1]
5        s.clear()
6        for i in a:
7            s.append(i)
8        