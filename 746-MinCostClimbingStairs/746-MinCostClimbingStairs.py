# Last updated: 9/21/2026, 4:06:00 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: list[int]) -> int:
3        cost.append(0)
4        for i in range(len(cost)-3,-1,-1):
5            cost[i]+=min(cost[i+1],cost[i+2])
6        return min(cost[0],cost[1])