# Last updated: 10/11/2026, 10:45:16 PM
1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        for i in range(1,n+1):
4            # print(sum([x for x in range(i)]),sum([y for y in range(i+1,n+1)]))
5            if sum([x for x in range(i)])==sum([y for y in range(i+1,n+1)]):
6                return i
7        return -1