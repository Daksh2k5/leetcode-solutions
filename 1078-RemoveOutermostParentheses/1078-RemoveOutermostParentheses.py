# Last updated: 8/9/2026, 12:36:02 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0
        for i in s:
            if i == '(':
                if count > 0:
                    ans.append(i)
                count +=1
            else:
                count -= 1
                if count > 0:
                    ans.append(i)
        return ''.join(ans)