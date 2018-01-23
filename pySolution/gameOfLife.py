class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)+2
        m = len(board[0])+2
        new_board = [[0]*m for _ in range(n)]
        nei = [[0]*m for _ in range(n)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                new_board[i+1][j+1] = board[i][j]

        for i in range(1, len(new_board)-1):
            for j in range(1, len(new_board[i])-1):
                if new_board[i][j] == 1:
                    nei[i+1][j+1] += 1
                    nei[i][j+1] += 1
                    nei[i-1][j+1] += 1
                    nei[i-1][j] += 1
                    nei[i+1][j] += 1
                    nei[i-1][j-1] += 1
                    nei[i][j-1] += 1
                    nei[i+1][j-1] += 1
        print(nei)

        for i in range(1,len(nei)-1):
            for j in range(1, len(nei[i])-1):
                if board[i-1][j-1] == 1:
                    if nei[i][j] < 2:
                        board[i-1][j-1] = 0
                    elif 2 <= nei[i][j] <= 3:
                        board[i-1][j-1] = 1
                    elif nei[i][j] > 3:
                        board[i-1][j-1] = 0
                else:
                    if nei[i][j] == 3:
                        board[i-1][j-1] = 1

temp = [[1,1],[1,0]]
Solution().gameOfLife(temp)
print(temp)