import collections


class Solution:
    def isInterleave(self, s1, s2, s3):
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        dp = [[True]*(len_s1+1) for _ in range(len_s2+1)]
        for i in range(1, len_s2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1] == s3[i-1]
        for i in range(1, len_s1+1):
            dp[0][i] = dp[0][i-1] and s1[i-1] == s3[i-1]
        for i in range(1, len_s2+1):
            for j in range(1, len_s1+1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i+j-1]) or (dp[i][j-1] and s1[j-1] == s3[i+j-1])
        print(dp)
        return dp[-1][-1]

s = Solution().isInterleave("aabcc",
                            "dbbbca",
                            "aadbbbcbcac")
print(s)
