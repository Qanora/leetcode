class Solution:
    def wordBreak(self, s, wordDict):
        ans = [[-1] for _ in range(len(s)+1)]
        for i in range(len(s) + 1):
            for j in range(0, i):
                if ans[i]
s = Solution().wordBreak("cars",["car","ca","rs"])
print(s)