# Last updated: 8/9/2026, 12:35:51 PM
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        n=len(grid[0])
        for i in grid:
            for j in i:
                l.append(j)
        k=k%len(l)
        l[:] = l[-k:] + l[:-k]
        
        grid=[]
        for i in range(0,len(l),n):
            grid.append(l[i:i+n])
        return grid