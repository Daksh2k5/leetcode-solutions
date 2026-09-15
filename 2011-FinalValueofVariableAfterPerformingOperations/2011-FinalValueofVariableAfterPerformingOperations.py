# Last updated: 9/15/2026, 4:45:14 PM
1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        x=0
4        for i in operations:
5            if i =="--X" or i == "X--":
6                x-=1
7            else:
8                x+=1
9        return x