# Last updated: 10/12/2026, 8:03:52 PM
1class Solution:
2    def coinChange(self, coins: list[int], amount: int) -> int:
3        dp=[]
4        if amount == 0:
5            return 0
6
7        if amount<min(coins):
8            return -1
9        
10        if amount in coins:
11            return 1
12        for _ in range(amount):
13            dp.append(-1)
14
15        for i in sorted(coins):
16            try:
17                dp[i-1]=1
18            except IndexError:
19                break
20
21        for i in range(len(dp)):
22            if dp[i]==-1:
23                dp[i]=float('inf')
24                for j in coins:
25                    if j<amount:
26                        if i-j>-1 and dp[i-j]!=-1:
27                            dp[i]=min(dp[i],dp[i-j]+1)
28
29        return dp[amount-1] if dp[amount-1] != float('inf') else -1