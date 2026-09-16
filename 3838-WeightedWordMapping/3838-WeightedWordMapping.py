# Last updated: 9/16/2026, 10:30:18 PM
1class Solution:
2    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
3        ans = ""
4        for w in words:
5            s = 0
6            for i in w:
7                s += weights[ord(i) - ord("a")]
8            ans += chr(ord("z") - (s % 26))
9        return ans