# Last updated: 8/9/2026, 12:35:30 PM
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        res=""
        mid=""
        d={}
        s=[x for x in s]
        for i in s:
            d[i]=d.get(i,0)+1
        d = dict(sorted(d.items()))
        # print(d)
        for key in d:
            if d[key]%2==0:
                for i in range(d[key]//2):
                    res+=key
            else:
                mid+=key
                for i in range((d[key]-1)//2):
                    res+=key
        return(res+mid+res[::-1])
