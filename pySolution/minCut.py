class Solution:
    def minCut(self, s):
        dp = [[0]*len(s) for _ in range(len(s))]
        if not s:
            return 0
        rvs = s[::-1]
        count = 0
        for i in range(len(rvs)):
            for j in range(len(s)):
                if rvs[i] == s[j]:
                    dp[i][j] = 1
        ans = [0]*len(s)

        for i in range(0, len(s)-1):
            # print(i, len(s)-i-1, self.getX(dp, i, len(s)-i-1), self.getTriangle(dp, i, len(s)-i-1))
            ans[len(s)-i-1] = max(ans[len(s)-i-1], self.getX(dp, i, len(s)-i-1))
            ans[len(s)-i-1] = max(ans[len(s)-i-1], self.getTriangle(dp, i, len(s)-i-1))
        print(ans)

        temp = [0]*len(s)
        for i in range(len(s)):
            temp[i-ans[i]//2] = ans[i]
        print(temp)

        count = 0
        for i in range(len(s)):
            if count < temp[i]:
                count = temp[i]
            elif count != 0:
                temp[i] = 0
                count -= 1
        print(temp)

        count = 0
        for val in temp:
            if val != 0:
                count += val
                count -= 1

        return len(s) - 1 - count

    def getX(self, dp, i, j):
        width = 1
        while True:
            if i - width >= 0 and i + width <= len(dp)-1 and j - width >= 0 and j + width <= len(dp)-1 \
                    and dp[i-width][j-width] == 1 and dp[i+width][j+width] == 1:
                width += 1
            else:
                break
        return 2 * (width-1) + 1

    def getTriangle(self, dp, i, j):
        count = 0
        up = [i, j - 1]
        down = [i + 1, j]
        while True:
            if 0 <= up[0] < len(dp) and 0 <= up[1] < len(dp) and 0 <= down[0] < len(dp) and 0 <= down[1] < len(dp) \
                    and dp[up[0]][up[1]] == 1 and dp[down[0]][down[1]] == 1:
                up[0] -= 1
                up[1] -= 1
                down[0] += 1
                down[1] += 1
                count += 1
            else:
                break
        if count == 0:
            return 1
        return 2 * count

    def getMaxCount(self, count, index, sum):
        if index == len(count)-1:
            return sum
        for i in range(index, len(count)):
            temp = sum+count[i]-1 if count[i] != 1 else sum
            sum = max(sum,self.getMaxCount(count, index+count[i], temp))
        return sum
#s = Solution().minCut("ccaacabacb")
#print(s)

s = Solution().getMaxCount([2, 4, 1, 3, 5, 1, 1, 1, 1, 1], 0, 0)
print(s)