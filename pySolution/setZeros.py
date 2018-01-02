class Solution:
    def setZeroes(self, matrix):
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ans.append((i,j))
        while ans:
            position = ans.pop()
            for i in range(len(matrix)):
                matrix[i][position[1]] = 0
            for i in range(len(matrix[0])):
                matrix[position[0]][i] = 0
        print(ans)

Solution().setZeroes()