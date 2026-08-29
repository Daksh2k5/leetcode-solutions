# Last updated: 8/29/2026, 3:22:29 PM
1class Solution:
2    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
3        ans=[]
4        for i in matrix:
5            ans.append(sum(i))
6        return ans