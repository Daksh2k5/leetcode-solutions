# Last updated: 8/7/2026, 9:38:33 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        mini=prices[0]
4        maxi=0
5        l=[]
6        for i in prices:
7            maxi=max(maxi,i)
8            if i < mini:
9                l.append(maxi-mini)
10                mini=i
11                maxi=0
12        l.append(maxi-mini)
13        return max(l)