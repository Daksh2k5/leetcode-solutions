# Last updated: 8/18/2026, 1:24:56 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        left=0
        right=len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left]!=s[right]:
                return False
            else:
                left+=1
                right-=1
        return True