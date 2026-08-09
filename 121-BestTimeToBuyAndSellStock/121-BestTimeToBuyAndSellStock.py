# Last updated: 8/9/2026, 12:37:16 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=0
        l=[]
        for i in prices:
            maxi=max(maxi,i)
            if i < mini:
                l.append(maxi-mini)
                mini=i
                maxi=0
        l.append(maxi-mini)
        return max(l)