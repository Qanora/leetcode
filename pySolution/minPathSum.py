class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 :
                    if j == 0:
                        ans[i][j] = grid[i][j]
                    else:
                        ans[i][j] = ans[i][j-1] + grid[i][j]
                else:
                    if j == 0:
                        ans[i][j] = ans[i-1][j] + grid[i][j]
                    else:
                        ans[i][j] = min(ans[i-1][j],ans[i][j-1]) + grid[i][j]
        return ans[-1][-1]

s = Solution().minPathSum([[1]])
print(s)