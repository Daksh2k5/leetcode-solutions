# Last updated: 7/9/2026, 11:22:54 PM
'''
im really embarrassed by this solution
i'll improve this someday
'''

1class Solution:
2    def isValid(self, s: str) -> bool:
3        l=['z']
4        for i in s:
5            if i == '(' or i == '{' or i == '[':
6                l.append(i)
7            if i == ')':
8                if '(' not in l:
9                    return False
10            if i == '}':
11                if '{' not in l:
12                    return False
13            if i == ']':
14                if '[' not in l:
15                    return False
16
17
18            if i == ')':
19                if l[-1]=='(':
20                    l.pop()
21            if i == '}': 
22                if l[-1]=='{':
23                    l.pop()
24            if i == ']': 
25                if l[-1]=='[':
26                    l.pop()
27        print(l)
28        if len(l)==1:
29            return True
30        return False