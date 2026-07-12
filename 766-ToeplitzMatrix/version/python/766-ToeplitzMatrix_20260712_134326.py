# Last updated: 7/12/2026, 1:43:26 PM
# i did not understand the question the first i attempted it
1class Solution:
2    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
3        for i in range(len(matrix)-1):
4            for j in range(len(matrix[0])-1):
5                if matrix[i][j]!=matrix[i+1][j+1]:
6                    return False
7        return True     
8        