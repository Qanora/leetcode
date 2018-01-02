class Solution:
    def combine(self, n, k):
        self.rList = []
        s = self.dfs(n, 0, k, 0,[])
        print(self.rList)
        return self.rList

    def dfs(self, n, last, k, deep, ans):
        if deep == k :
            self.rList.append(ans)
            return
        for i in range(last+1, n+1):
                self.dfs(n, i, k, deep+1, ans+[i])
        return
Solution().combine(4,3)