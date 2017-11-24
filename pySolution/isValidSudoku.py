class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.check_col(board) and self.check_row(board) and self.check_range(board):
            return True
        return False

    def check_row(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                for k in range(j+1,len(board),1):
                    if board[i][j] != '.' and board[i][j] == board[i][k]:
                        print("check_row")
                        return False
        return True

    def check_col(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                for k in range(j+1,len(board),1):
                    if board[j][i] != '.' and board[j][i] == board[k][i]:
                        print("check_col")
                        return False
        return True

    def check_range(self,board):
        for left in range(0, 7, 3):
            for right in range(0, 7, 3):
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            for g in range(3):
                                if board[i+left][j+right] != '.' and board[i+left][j+right] == board[k+left][g+right] and (i != k and j != g):
                                    print(i+left,j+right,k+left,g+right)
                                    print("check_range")
                                    return False
        return True

board = [[".",".","5",".",".",".",".",".","6"],
         [".",".",".",".","1","4",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".","9","2",".","."],
         ["5",".",".",".",".","2",".",".","."],
         [".",".",".",".",".",".",".","3","."],
         [".",".",".","5","4",".",".",".","."],
         ["3",".",".",".",".",".","4","2","."],
         [".",".",".","2","7",".","6",".","."]]
s = Solution().isValidSudoku(board)

print(s)
