# Last updated: 11/15/2026, 11:45:41 PM
1class Solution:
2    def findWords(self, words: list[str]) -> list[str]:
3        a = set("qwertyuiop")
4        b = set("asdfghjkl")
5        c = set("zxcvbnm")
6        ans = []
7        for word in words:
8            word_set = set(word.lower())
9            if word_set.issubset(a) or word_set.issubset(b) or word_set.issubset(c):
10                ans.append(word)
11                
12        return ans