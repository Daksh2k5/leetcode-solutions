# Last updated: 9/13/2026, 4:09:07 PM
1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        count=0
4        for i in jewels:
5            count+=stones.count(i)
6        return count