# Last updated: 10/13/2026, 12:56:50 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        mini=prices[0]
4        maxi=0
5        l=float('-inf')
6        for i in prices:
7            maxi=max(maxi,i)
8            if i < mini:
9                # l.append(maxi-mini)
10                mini=i
11                maxi=0
12            l=max(l,maxi-mini)
13        return l