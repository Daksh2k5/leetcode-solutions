# Last updated: 8/5/2026, 11:22:14 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l=[]
4        m=0
5        for i in s:
6            if i not in l:
7                l.append(i)
8                m=max(len(l),m)
9            else:
10                l=l[l.index(i)+1:]
11                l.append(i)
12                m=max(len(l),m)
13        return(m)