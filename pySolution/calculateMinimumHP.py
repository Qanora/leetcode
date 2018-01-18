import copy
class Solution:
    # def calculateMinimumHP(self, dungeon):
    #     dungeon = dungeon[::-1]
    #     for i in range(len(dungeon)):
    #         dungeon[i] = dungeon[i][::-1]
    #     print(dungeon)
    #     addTemp = copy.deepcopy(dungeon)
    #     maxTemp = copy.deepcopy(dungeon)
    #     col = len(dungeon)
    #     row = len(dungeon[0])
    #     for i in range(1, row):
    #         addTemp[0][i] = addTemp[0][i-1] + addTemp[0][i]
    #         maxTemp[0][i] = min(maxTemp[0][i-1], addTemp[0][i])
    #     for i in range(1, col):
    #         addTemp[i][0] = addTemp[i-1][0] + addTemp[i][0]
    #         maxTemp[i][0] = min(maxTemp[i-1][0], addTemp[i][0])
    #     if col != 1 and row != 1:
    #         for i in range(1, col):
    #             for j in range(1, row):
    #                 if maxTemp[i-1][j] > maxTemp[i][j-1]:
    #                     addTemp[i][j] = addTemp[i][j] + addTemp[i-1][j]
    #                     maxTemp[i][j] = min(addTemp[i][j], maxTemp[i-1][j])
    #                 else:
    #                     addTemp[i][j] = addTemp[i][j] + addTemp[i][j-1]
    #                     maxTemp[i][j] = min(addTemp[i][j], maxTemp[i][j-1])
    #     print(maxTemp, addTemp)
    #     if addTemp[-1][-1] > 0:
    #         return 1
    #     else:
    #         return abs(addTemp[-1][-1]) + 1

    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        # If at any point his health point drops to 0 or below, he dies immediately.
        # have to make sure at any point health is > 0
        # dp[i][j] is minimum health needed when arriving at this grid
        # dp[i][j] = min(max(1, dp[right]-right_grid_value), max(1, dp[down]-down_grid_value))
        row, col = len(dungeon), len(dungeon[0])
        dp = [[0 for x in range(col)] for x in range(row)]
        dp[row - 1][col - 1] = 1
        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = max(1, dp[i + 1][col - 1] - dungeon[i + 1][col - 1])
            print(dp)
        for i in range(col - 2, -1, -1):
            dp[row - 1][i] = max(1, dp[row - 1][i + 1] - dungeon[row - 1][i + 1])
            print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                right = max(1, dp[i][j + 1] - dungeon[i][j + 1])
                down = max(1, dp[i + 1][j] - dungeon[i + 1][j])
                dp[i][j] = min(right, down)
        return max(1, dp[0][0] - dungeon[0][0])

s = Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
print(s)