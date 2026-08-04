# Last updated: 8/4/2026, 11:07:30 AM
# idk how i'll do this in an interview
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        rows=len(matrix[0])
4        cols=len(matrix)
5        tl=rows*cols
6        ans=[]
7        while (True):
8            ans.extend(matrix[0])
9            if len(ans)==tl:
10                break
11
12            for i in range(1,len(matrix)):
13                ans.append(matrix[i][-1])
14            if len(ans)==tl:
15                break
16
17            ll=matrix[-1][:0:-1][1:]
18            ans.extend(ll)
19            if len(ans)==tl:
20                break
21
22            fl=[]
23            for i in range(1,len(matrix)):
24                fl.append(matrix[i][0])
25            fl=fl[::-1]
26            ans.extend(fl)
27            if len(ans)==tl:
28                break
29
30            newmat=[]
31            for i in matrix[1:-1]:
32                newmat.append(i[1:-1])
33            matrix=newmat.copy()
34        return ans