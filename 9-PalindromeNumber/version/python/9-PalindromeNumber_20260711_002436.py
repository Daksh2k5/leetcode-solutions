# Last updated: 7/11/2026, 12:24:36 AM
# i don't know how to optimise this any further
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if str(x)==str(x)[::-1]:
4            return True
5        return False