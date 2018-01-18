class Solution:
    def combinationSum3(self, k, n):
        self.rAns = []
        self.dfs([],k,n,1)
        return self.rAns

    def dfs(self, ans, k, n, start):
        if len(ans) == k and n == 0:
            self.rAns.append(ans[:])
            return
        for i in range(start, 10):
            ans.append(i)
            self.dfs(ans, k, n-i, i+1)
            ans.pop()

s = Solution().combinationSum3(3,9)
print(s)