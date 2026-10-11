# Last updated: 10/11/2026, 10:49:07 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if str(x) == str(x)[::-1]:
4            return True
5        else:
6            return False