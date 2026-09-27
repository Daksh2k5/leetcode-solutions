# Last updated: 9/23/2026, 6:51:29 PM
1class Solution:
2    def countBits(self, n: int) -> list[int]:
3        res = [0] * (n + 1)
4        for i in range(1, n + 1):
5            if i % 2 == 0:
6                res[i] = res[i // 2]
7            else:
8                res[i] = res[i - 1] + 1
9        return res
10