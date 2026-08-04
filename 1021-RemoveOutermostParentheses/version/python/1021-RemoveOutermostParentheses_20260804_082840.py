# Last updated: 8/4/2026, 8:28:40 AM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        ans = []
4        count = 0
5        for i in s:
6            if i == '(':
7                if count > 0:
8                    ans.append(i)
9                count +=1
10            else:
11                count -= 1
12                if count > 0:
13                    ans.append(i)
14        return ''.join(ans)