# Last updated: 9/5/2026, 1:35:46 PM
from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score=0
        n=[int(x) for x in str(n)]
        c=Counter(n)
        for i in c:
            score+= c[i]*i
        return score