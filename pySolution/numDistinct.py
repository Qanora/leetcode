class Solution:
    def numDistinct(self, s, t):
        ans = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            ans[0][i] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    ans[i+1][j+1] = ans[i][j] + ans[i+1][j]
                else:
                    ans[i+1][j+1] = ans[i+1][j]
        return ans[-1][-1]
s = Solution().numDistinct("aacaaaca","ca")
print(s)