class Solution:
    def numSquares(self, n):
        ans = []
        for i in range(1, n):
            if i*i <= n:
                ans.append(i*i)
            else:
                break
        ans.reverse()
        self.dict = {}
        return self.dfs(n, ans)

    def dfs(self, n, dict):
        if n in self.dict:
            return self.dict.get(n)
        total = 0
        count = 0
        rans = n
        for i, val in enumerate(dict):
            if n - total == 0:
                self.dict[n] = rans
                return rans
            if n - total >= val:
                add_count = (n - total) // val
                count += add_count
                add_total = ((n - total) // val) * val
                total += add_total
                rans = min(self.dfs(n-total, dict[i+1:])+count, rans)
                total -= add_total
                count -= add_count
        return rans

s = Solution().numSquares(6175)
print(s)
