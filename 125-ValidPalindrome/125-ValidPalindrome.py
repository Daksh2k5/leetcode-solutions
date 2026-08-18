# Last updated: 8/18/2026, 1:24:56 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s=s.lower()
4        left=0
5        right=len(s)-1
6        while left<right:
7            if not s[left].isalnum():
8                left+=1
9                continue
10            if not s[right].isalnum():
11                right-=1
12                continue
13            if s[left]!=s[right]:
14                return False
15            else:
16                left+=1
17                right-=1
18        return True