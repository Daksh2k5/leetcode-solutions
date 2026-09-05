# Last updated: 9/5/2026, 1:35:46 PM
1from collections import Counter
2class Solution:
3    def digitFrequencyScore(self, n: int) -> int:
4        score=0
5        n=[int(x) for x in str(n)]
6        c=Counter(n)
7        for i in c:
8            score+= c[i]*i
9        return score