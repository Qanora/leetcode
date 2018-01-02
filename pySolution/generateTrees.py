class Solution:
    def generateTrees(self, n):
        self.ans = [0,1,2]
        if n < 3:
            return self.ans[n]
        self.generate(n)
        return self.ans[-1]

    def generate(self, n):
        if n > 2:
            self.ans.append(self.ans[-1]*2+self.ans[-2])
            self.generate(n-1)


s = Solution().generateTrees(4)
print(s)