# Last updated: 8/9/2026, 12:38:09 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        return False