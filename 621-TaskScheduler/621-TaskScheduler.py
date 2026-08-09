# Last updated: 8/9/2026, 12:36:29 PM
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=list(Counter(tasks).values())
        m=max(c)
        c=c.count(m)
        return(max((n*(m-1)+m)+(c-1),len(tasks)))