class Solution:
    def wordBreak(self, s, wordDict):
        ans = [False] * (len(s)+1)
        ans[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if ans[j] and s[j:i] in wordDict:
                    ans[i] = True
        return ans[-1]
s = Solution().wordBreak("cars",["car","ca","rs"])
print(s)