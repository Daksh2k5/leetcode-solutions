# Last updated: 7/20/2026, 7:45:47 PM
# probably not the intended solution
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        l=[]
4        n=len(grid[0])
5        for i in grid:
6            for j in i:
7                l.append(j)
8        k=k%len(l)
9        l[:] = l[-k:] + l[:-k]
10        
11        grid=[]
12        for i in range(0,len(l),n):
13            grid.append(l[i:i+n])
14        return grid