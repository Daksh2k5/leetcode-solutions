# Last updated: 11/16/2026, 8:59:44 AM
1class Solution:
2    def digitSum(self, s: str, k: int) -> str:
3        while len(s) > k:
4            nexts = ""
5            
6            for i in range(0, len(s), k):
7                chunk = s[i : i + k]
8                
9                total = 0
10                for digit in chunk:
11                    total += int(digit)
12                    
13                nexts += str(total)
14
15            s = nexts
16        return s