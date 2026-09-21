# Last updated: 9/21/2026, 3:55:49 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: list[int]) -> int:
3        dp=cost.copy()
4        dp.append(0)
5        for i in range(len(cost)-2,-1,-1):
6            # print(dp[i])
7            dp[i]+=min(dp[i+1],dp[i+2])
8        # print(dp)
9        return min(dp[0],dp[1])