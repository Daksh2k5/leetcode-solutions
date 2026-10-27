# Last updated: 10/27/2026, 9:23:50 AM
1class Solution:
2    def createGrid(self, m: int, n: int) -> list[str]:
3        ans=["."*n]
4        for i in range(m-1):
5            ans.append("#"*(n-1)+".")
6        return ans