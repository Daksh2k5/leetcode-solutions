# Last updated: 8/14/2026, 12:28:32 PM
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        s.split()
        maxi=0
        subs=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                subs.append(s[i:j])
        for i in subs:
            c=sorted(Counter(i).values(),reverse=True)
            if c[0]<3:
                maxi=max(maxi,len(i))
        return maxi