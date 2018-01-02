class Solution:
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        ans = []
        for _ in range(rowIndex+1):
            ans.insert(0,1)
            for i in range(1,len(ans)-1):
                ans[i] = ans[i] + ans[i+1]
        return ans

s = Solution().getRow(4)
print(s)