# Last updated: 9/16/2026, 10:30:18 PM
class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans = ""
        for w in words:
            s = 0
            for i in w:
                s += weights[ord(i) - ord("a")]
            ans += chr(ord("z") - (s % 26))
        return ans