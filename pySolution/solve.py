class Solution:
    def solve(self, board):
        quene = []
        if board:
            m = len(board)
            n = len(board[0])

            for i in range(len(board[0])):
                if board[0][i] == 'O':
                    quene.append([0,i])
                if board[-1][i] == 'O':
                    quene.append([m-1,i])

            for i in range(len(board)):
                if board[i][0] == 'O':
                    quene.append([i,0])
                if board[i][-1] == 'O':
                    quene.append([i,n-1])

            direct = [(0,0),(0,-1),(0,1),(1,0),(-1,0)]

            while quene:
                temp = quene.pop()
                board[temp[0]][temp[1]] = 'I'
                self.dfs(direct, board, temp)

            for val in board:
                print(val)

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 'I':
                        board[i][j] = "O"
                    else:
                        board[i][j] = "X"

    def dfs(self, direct, board, index):
        for val in direct:
            if index[0] + val[0] >= 0 and index[0] + val[0] < len(board) and \
                                    index[1] + val[1] >= 0 and index[1] + val[1] < len(board[0]):
                if board[index[0] + val[0]][index[1] + val[1]] == 'O':
                    board[index[0]][index[1]] = 'I'
                    index[0] += val[0]
                    index[1] += val[1]
                    self.dfs(direct, board, index)
                    index[0] -= val[0]
                    index[1] -= val[1]

Solution().solve([["O","X","X","O","X"],
                  ["X","O","O","X","O"],
                  ["X","O","X","O","X"],
                  ["O","X","O","O","O"],
                  ["X","X","O","X","O"]])

"""[["O","X","X","O","X"],
 ["X","O","O","X","O"],
 ["X","O","X","O","X"],
 ["O","X","O","O","O"],
 ["X","X","O","X","O"]]

[["O","X","X","O","X"],
 ["X","X","X","X","O"],
 ["X","X","X","X","X"],
 ["O","X","O","O","O"],
 ["X","X","O","X","O"]]

[["O","X","X","O","X"],
 ["X","X","X","X","O"],
 ["X","X","X","O","X"],
 ["O","X","O","O","O"],
 ["X","X","O","X","O"]]"""