# Last updated: 8/9/2026, 12:37:15 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans="".join([x for x in s if x.isalnum()]).lower()
        return (ans==ans[::-1])