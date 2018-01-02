import copy


class Solution:
    def totalNQueens(self, n):
        self.solution = 0
        temp = [["." for _ in range(n)] for _ in range(n)]
        self.solve(temp, 0, n)
        if n == 0:
            return 0
        return self.solution

    def solve(self, temp, deep, n):
        if deep == n:
            self.solution += 1
            return
        for i in range(n):
            if self.detect(temp, deep, i, n):
                temp[deep][i] = 'Q'
                self.solve(temp, deep+1, n)
                temp[deep][i] = '.'


    def detect(self, temp , col ,row, n):
        for i in range(n):
            if temp[col][i] == 'Q':
                return False
            if temp[i][row] == 'Q':
                return False

        for i in range(n):
            for j in range(n):
                if (i - j) == (col - row) and temp[i][j] == 'Q':
                    return False
                if (i + j) == (col + row) and temp[i][j] == 'Q':
                    return False
        return True

for i in range(10):
    s = Solution().totalNQueens(i)
    print(i,s)