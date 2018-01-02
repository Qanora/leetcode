class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(0,len(matrix)-1):
            for j in range(len(matrix[0])):
                if matrix[i+1][j] != 0 and matrix[i][j] != 0:
                    matrix[i+1][j] = matrix[i][j] + 1
        return  max(self.getRowMax(row) for row in matrix)

    def getRowMax(self, height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                print(h*w)
                size = max(size, h*w)
            stack.append(i)
        return size

Solution().maximalRectangle([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])