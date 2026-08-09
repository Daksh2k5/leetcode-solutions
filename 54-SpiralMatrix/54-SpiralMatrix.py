# Last updated: 8/9/2026, 12:37:36 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix[0])
        cols=len(matrix)
        tl=rows*cols
        ans=[]
        while (True):
            ans.extend(matrix[0])
            if len(ans)==tl:
                break

            for i in range(1,len(matrix)):
                ans.append(matrix[i][-1])
            if len(ans)==tl:
                break

            ll=matrix[-1][:0:-1][1:]
            ans.extend(ll)
            if len(ans)==tl:
                break

            fl=[]
            for i in range(1,len(matrix)):
                fl.append(matrix[i][0])
            fl=fl[::-1]
            ans.extend(fl)
            if len(ans)==tl:
                break

            newmat=[]
            for i in matrix[1:-1]:
                newmat.append(i[1:-1])
            matrix=newmat.copy()
        return ans