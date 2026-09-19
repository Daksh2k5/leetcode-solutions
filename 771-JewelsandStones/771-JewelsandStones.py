# Last updated: 9/13/2026, 4:09:07 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            count+=stones.count(i)
        return count