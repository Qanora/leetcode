class Solution:
    def exist(self, board, word):
        self.path = []
        start = []
        direct = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    start.append([i,j])

        for val in start:
            self.path.append((val[0], val[1]))
            if self.dfs(board, direct, val, word, 1):
                return True
            self.path.pop()
        return False

    def dfs(self, board, direct, currentPosition, word, wordIndex):
        position = [0, 0]
        if wordIndex == len(word):
            return True
        for step in direct:
            position[1] = currentPosition[1] + step[1]
            position[0] = currentPosition[0] + step[0]
            if position[1] >= 0 and position[1] < len(board[0]) and position[0] >= 0 and position[0] < len(board):
                if (position[0], position[1]) not in self.path and board[position[0]][position[1]] == word[wordIndex]:
                    self.path.append((position[0],position[1]))
                    if self.dfs(board, direct, position, word, wordIndex+1):
                        return True
                    self.path.pop()
        return False

s = Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
print(s)