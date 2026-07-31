# Last updated: 7/31/2026, 4:32:08 PM
1from collections import Counter
2class Solution:
3    def minimumPushes(self, word: str) -> int:
4        s=dict(Counter(word).most_common())
5        x=0
6        count=0
7        for i in s:
8            count+=(s[i] *((x//8)+1))
9            x+=1
10
11        return(count)