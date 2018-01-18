class Solution:
    def numIslands(self, grid):
        grid.insert(0, ['0']*len(grid[0]))
        grid.append(['0']*len(grid[0]))
        for i in range(len(grid)):
            grid[i].insert(0,'0')
            grid[i].append('0')
        count = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == '1':
                    self.disable(grid, i, j)
                    grid[i][j] = '1'

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == '1':
                    count += 1
        return count

    def disable(self, grid, i, j):
        grid[i][j] = '0'
        if grid[i+1][j] == '1':
            self.disable(grid, i+1, j)
        if grid[i-1][j] == '1':
            self.disable(grid, i - 1, j)
        if grid[i][j-1] == '1':
            self.disable(grid, i, j - 1)
        if grid[i][j+1] == '1':
            self.disable(grid, i, j + 1)

s = Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(s)