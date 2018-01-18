import math


class Solution:

    def maximalSquare(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 1:
                    matrix[i][j] = pow(int(math.sqrt(min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]))) + 1, 2)

        count = 0
        for temp in matrix:
            print(temp)
            count = max(count,max(temp))
        return count

ans = [[1,0,1,0,0],
       [1,0,1,1,1],
       [1,1,1,1,1],
       [1,0,0,1,0]]
s = Solution().maximalSquare(ans)

print(s)