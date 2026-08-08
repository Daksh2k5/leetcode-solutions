# Last updated: 8/8/2026, 2:36:41 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        for l in board:
4            l=[x for x in l if x != "."]
5            if sorted(l) != sorted(set(l)):
6                return False
7        for i in range(9):
8            l=[board[0][i],board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i],board[7][i],board[8][i]]
9            l=[x for x in l if x != "."]
10            if sorted(l) != sorted(set(l)):
11                return False
12        for i in range(0,9,3):
13            l=board[i][0:3]+board[i+1][0:3]+board[i+2][0:3]
14            l=[x for x in l if x != "."]
15            if sorted(l) != sorted(set(l)):
16                return False
17            l=board[i][3:6]+board[i+1][3:6]+board[i+2][3:6]
18            l=[x for x in l if x != "."]
19            if sorted(l) != sorted(set(l)):
20                return False
21            l=board[i][6:9]+board[i+1][6:9]+board[i+2][6:9]
22            l=[x for x in l if x != "."]
23            if sorted(l) != sorted(set(l)):
24                return False
25        return True