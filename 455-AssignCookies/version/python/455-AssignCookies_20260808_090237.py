# Last updated: 8/8/2026, 9:02:37 AM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        ans=0
4        g.sort()
5        s=dict(Counter(sorted(s)))
6        for i in g:
7            for j in s:
8                if j >= i:
9                    ans+=1
10                    s[j]-=1
11                    if s[j]==0:
12                        del s[j]
13                        break
14                    break
15        return ans