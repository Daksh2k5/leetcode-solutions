# Last updated: 7/11/2026, 5:50:30 PM
# took me way to long to figure out
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        result = [[1]]
4        for i in range(numRows - 1):
5            temp = [0] + result[-1] + [0]
6            x = []
7            for j in range(len(temp) - 1):
8                x.append(temp[j] + temp[j + 1])
9            result.append(x)
10        return result
11