class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        self.ans = [0,1]
        self.dfs(n, 1)
        return self.ans

    def dfs(self, n, index):
        if n <= index:
            return
        for val in self.ans[::-1]:
            self.ans.append(val+pow(2,index))
        self.dfs(n, index+1)

s = Solution().grayCode(4)
print(s)
