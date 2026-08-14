# Last updated: 8/14/2026, 12:28:32 PM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        s.split()
4        maxi=0
5        subs=[]
6        for i in range(len(s)):
7            for j in range(i+1,len(s)+1):
8                subs.append(s[i:j])
9        for i in subs:
10            c=sorted(Counter(i).values(),reverse=True)
11            if c[0]<3:
12                maxi=max(maxi,len(i))
13        return maxi