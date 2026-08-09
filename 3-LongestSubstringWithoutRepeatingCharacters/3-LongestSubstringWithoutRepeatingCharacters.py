# Last updated: 8/9/2026, 12:38:11 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        m=0
        for i in s:
            if i not in l:
                l.append(i)
                m=max(len(l),m)
            else:
                l=l[l.index(i)+1:]
                l.append(i)
                m=max(len(l),m)
        return(m)