# Last updated: 8/29/2026, 3:22:29 PM
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        for i in matrix:
            ans.append(sum(i))
        return ans