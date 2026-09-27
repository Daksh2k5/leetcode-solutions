# Last updated: 9/23/2026, 12:11:15 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l=0
4        r=1
5        ml=0
6        while r<len(s)+1:
7            window=s[l:r]
8            c=Counter(window)
9            if c.most_common(1)[0][1]<2:
10                ml=max(ml,r-l)
11                r+=1
12                continue
13            else:
14                l+=1
15        return(ml)