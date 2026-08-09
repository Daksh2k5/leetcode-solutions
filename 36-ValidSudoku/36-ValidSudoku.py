# Last updated: 8/9/2026, 12:37:44 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            l=[x for x in l if x != "."]
            if sorted(l) != sorted(set(l)):
                return False
        for i in range(9):
            l=[board[0][i],board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i],board[7][i],board[8][i]]
            l=[x for x in l if x != "."]
            if sorted(l) != sorted(set(l)):
                return False
        for i in range(0,9,3):
            l=board[i][0:3]+board[i+1][0:3]+board[i+2][0:3]
            l=[x for x in l if x != "."]
            if sorted(l) != sorted(set(l)):
                return False
            l=board[i][3:6]+board[i+1][3:6]+board[i+2][3:6]
            l=[x for x in l if x != "."]
            if sorted(l) != sorted(set(l)):
                return False
            l=board[i][6:9]+board[i+1][6:9]+board[i+2][6:9]
            l=[x for x in l if x != "."]
            if sorted(l) != sorted(set(l)):
                return False
        return True