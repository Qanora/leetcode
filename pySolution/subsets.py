class Solution:
    def subsets(self, nums):
        self.rList = []
        k = len(nums)
        for i in range(1,k+1):
            self.combine(k,i, nums)
        self.rList.append([])
        print(self.rList)
        return self.rList

    def combine(self, n, k, nums):
        s = self.dfs(n, 0, k, 0, [], nums)

    def dfs(self, n, last, k, deep, ans, nums):
        if deep == k:
            self.rList.append(ans)
            return
        for i in range(last + 1, n + 1):
            self.dfs(n, i, k, deep + 1, ans + [nums[i-1]], nums)
        return

Solution().subsets([1,4,5])