# Last updated: 8/11/2026, 12:06:30 PM
class Solution:
    def isValid(self, s: str) -> bool:
        l=['z']
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            if i == ')':
                if '(' not in l:
                    return False
            if i == '}':
                if '{' not in l:
                    return False
            if i == ']':
                if '[' not in l:
                    return False


            if i == ')':
                if l[-1]=='(':
                    l.pop()
            if i == '}': 
                if l[-1]=='{':
                    l.pop()
            if i == ']': 
                if l[-1]=='[':
                    l.pop()
        print(l)
        if len(l)==1:
            return True
        return False