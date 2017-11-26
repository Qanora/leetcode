class Solution:
    def solveSudoku(self,board):
        self.solve(board)
        print(board)

    def isVaild(self, board, row, col,ch):
        if self.check_range(board,row,col,ch) and self.check_rc(board,row,col,ch):
            return True
        return False


    def check_rc(self, board, row, col, ch):
        for i in range(len(board)):
            if board[i][col] == ch:
                return False
            if board[row][i] == ch:
                return False
        return True

    def check_range(self, board, row, col, ch):
        row_block = int(row/3)*3
        col_block = int(col/3)*3
        for i in range(row_block, row_block+3, 1):
            for j in range(col_block, col_block+3, 1):
                if board[i][j] == ch:
                    return False
        return True

    def solve(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    for num in [str(i) for i in range(1,10,1)]:
                        if self.isVaild(board,i,j,num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True


board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]
Solution().solveSudoku(board)
"""[["5","1","9","7","4","8","6","3","2"],
 ["7","8","3","6","5","2","4","1","9"],
 ["4","2","6","1","3","9","8","7","5"],
 ["3","5","7","9","8","6","2","4","1"],
 ["2","6","4","3","1","7","5","9","8"],
 ["1","9","8","5","2","4","3","6","7"],
 ["9","7","5","8","6","3","1","2","4"],
 ["8","3","2","4","9","1","7","5","6"],
 ["6","4","1","2","7","5","9","8","3"]]"""