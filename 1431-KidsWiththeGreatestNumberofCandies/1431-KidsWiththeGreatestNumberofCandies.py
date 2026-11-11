# Last updated: 11/11/2026, 4:11:09 PM
1class Solution:
2    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
3        m=max(candies)
4        ans=[]
5        for i in candies:
6            if i+extraCandies>=m:
7                ans.append(True)
8            else:
9                ans.append(False)
10        return ans