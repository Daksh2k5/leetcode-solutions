# Last updated: 7/30/2026, 2:47:16 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        if len(word)<=8:return len(word)
4        elif len(word)>8 and len(word)<=16:
5            return 8+((len(word)-8)*2)
6        elif len(word)>16 and len(word)<=24:
7            return 8+((len(word)-8)*2) + len(word)-16
8        elif len(word)==25:
9            return 8+((len(word)-8)*2) + len(word)-15
10        else:
11            return 8+((len(word)-8)*2) + len(word)-14