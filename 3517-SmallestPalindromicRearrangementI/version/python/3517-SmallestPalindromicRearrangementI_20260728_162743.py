# Last updated: 7/28/2026, 4:27:43 PM
# overcomplicated it initially but got there in the end
1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        res=""
4        mid=""
5        d={}
6        s=[x for x in s]
7        for i in s:
8            d[i]=d.get(i,0)+1
9        d = dict(sorted(d.items()))
10        # print(d)
11        for key in d:
12            if d[key]%2==0:
13                for i in range(d[key]//2):
14                    res+=key
15            else:
16                mid+=key
17                for i in range((d[key]-1)//2):
18                    res+=key
19        return(res+mid+res[::-1])
20