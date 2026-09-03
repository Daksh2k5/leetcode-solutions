# Last updated: 8/19/2026, 2:16:37 PM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        for i in patterns:
            if i in word:
                count+=1
        return count