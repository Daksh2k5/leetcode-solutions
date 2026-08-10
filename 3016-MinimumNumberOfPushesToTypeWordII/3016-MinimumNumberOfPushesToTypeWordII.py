# Last updated: 8/9/2026, 12:35:36 PM
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        s=dict(Counter(word).most_common())
        x=0
        count=0
        for i in s:
            count+=(s[i] *((x//8)+1))
            x+=1

        return(count)