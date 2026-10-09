# Last updated: 10/9/2026, 6:28:15 PM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        ans = 0
4        count = 0
5        for i in s:
6            if i == "(":
7                count += 2
8                if count % 2 == 1:
9                    ans += 1
10                    count -= 1
11            else:
12                count -= 1
13                if count < 0:
14                    ans += 1
15                    count = 1
16        return ans + count