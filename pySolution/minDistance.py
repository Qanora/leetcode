class Solution:
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1+1):
            dp[i][0] = i
        for i in range(len2+1):
            dp[0][i] = i
        for val1 in range(len1):
            for val2 in range(len2):
                if word1[val1] == word2[val2]:
                    dp[val1+1][val2+1] = dp[val1][val2]
                else:
                    dp[val1+1][val2+1] = min(dp[val1+1][val2],dp[val1][val2+1],dp[val1][val2])
                    dp[val1+1][val2+1] += 1
        return dp[-1][-1]

s = Solution().minDistance("","")
print(s)