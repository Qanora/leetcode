class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                obstacleGrid[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
        print(obstacleGrid)
        flag = False
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                flag = True
            if flag:
                obstacleGrid[i][0] = 0
        flag = False
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                flag = True
            if flag:
                obstacleGrid[0][i] = 0
        print(obstacleGrid)
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

s = Solution().uniquePathsWithObstacles([[0]])
print(s)