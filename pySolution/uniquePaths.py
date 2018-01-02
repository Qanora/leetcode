class Solution:
    def uniquePaths(self, m, n):
        ans = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[-1][-1]

s = Solution().uniquePaths(1,1)
print(s)