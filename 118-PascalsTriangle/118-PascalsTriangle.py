# Last updated: 8/9/2026, 12:37:19 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            x = []
            for j in range(len(temp) - 1):
                x.append(temp[j] + temp[j + 1])
            result.append(x)
        return result
