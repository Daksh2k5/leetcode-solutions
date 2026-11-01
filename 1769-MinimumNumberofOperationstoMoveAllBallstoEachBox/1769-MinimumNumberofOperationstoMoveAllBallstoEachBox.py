# Last updated: 11/2/2026, 1:28:30 AM
1class Solution:
2    def minOperations(self, boxes: str) -> list[int]:
3        n = len(boxes)
4        ans = [0]*n
5        for i in range(n):
6            for j in range(n):
7                if boxes[j]=='1':
8                    ans[i]+=abs(i - j)
9        return ans