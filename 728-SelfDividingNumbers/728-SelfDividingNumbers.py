# Last updated: 10/12/2026, 8:54:43 AM
1class Solution:
2    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
3        ans = []
4        for i in range(left, right + 1):
5            for j in str(i):
6                if int(j) == 0 or i % int(j) != 0:
7                    break
8            else:
9                ans.append(i)
10        return ans