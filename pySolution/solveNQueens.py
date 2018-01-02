import copy


class Solution:
    def solveNQueens(self, n):
        self.solution = []
        temp = [["." for _ in range(n)] for _ in range(n)]
        self.solve(temp, 0, n)
        print("fianl temp",id(temp))
        return self.solution

    def solve(self, temp, deep, n):
        if deep == n:
            print("temp",id(temp),temp)
            print("copy",id(copy.copy(temp)),copy.copy(temp))
            self.solution.append(copy.deepcopy(temp))
            for i in self.solution:
                print("solution",id(i),i)
            return
        for i in range(n):
            if self.detect(temp, deep, i, n):
                temp[deep][i] = 'Q'
                print("temp",id(temp),temp)
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

s = Solution().solveNQueens(4)
for i in s:
    print("final",id(i),i)
print(s)