# Last updated: 8/27/2026, 9:53:42 AM
1class Solution:
2    def diStringMatch(self, s: str) -> List[int]:
3        end=len(s)
4        start=0
5        ans=[]
6        for i in s:
7            if i == "I":
8                ans.append(start)
9                start+=1
10            else:
11                ans.append(end)
12                end-=1
13        if s[-1]=="I":
14            ans.append(ans[-1]+1)
15        else:
16            ans.append(ans[-1]-1)
17        return ans