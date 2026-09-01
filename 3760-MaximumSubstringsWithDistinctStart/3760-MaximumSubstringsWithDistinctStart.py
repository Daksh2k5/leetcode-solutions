# Last updated: 9/1/2026, 2:24:24 PM
class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = 0
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in s:
                ans += 1
        return ans