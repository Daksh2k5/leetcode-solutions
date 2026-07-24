# Last updated: 7/24/2026, 1:45:06 PM
'''
runtime- 7ms (81.23%*)
memory- 20.02 (31.77)
'''

1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        ans="".join([x for x in s if x.isalnum()]).lower()
4        return (ans==ans[::-1])