class Solution:
    def numTrees(self, n):
        self.ans = [1,1,2]
        if n == 0:
            return 0
        if n < 3:
            return self.ans[n]
        self.generate(n,3)
        return self.ans[-1]

    def generate(self, n, index):
        if index > n:
            return
        count = 0
        for val in range(1, index + 1):
            count += self.ans[(val-1)]* self.ans[(index-val)]
        self.ans.append(count)
        self.generate(n, index+1)

s = Solution().numTrees(5)
print(s)
