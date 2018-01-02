class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        prices.insert(0,prices[0])
        prices.append(prices[-1])
        buy = []
        sell = []
        for i in range(1,len(prices)-1):
            if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
                sell.append(prices[i])
            if prices[i-1] >= prices[i] and prices[i] < prices[i+1]:
                buy.append(prices[i])
        count = 0
        n = len(buy)
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                ans[i][j] = sell[j] - buy[i]

        count = [[0]*n for _ in range(n)]
        # for i in range(n-1):
        #     for j in range(i,n-1):
        #         temp = 0
        #         for k in range(j+1,n):
        #             temp = max(temp,max(ans[k]))
        #         count[i][j] = ans[i][j] + temp
        pre = 0
        for i in range(n-1,0,-1):
            pre = max(pre,max(ans[i]))
            for j in range(0,i):
                count[j][i-1] = ans[j][i-1] + pre
        print("count", count)
        maxCount = 0
        for i in range(n-1):
            for j in range(i,n-1):
                maxCount = max(maxCount,count[i][j])
        for i in range(n):
            for j in range(i,n):
                maxCount = max(maxCount, ans[i][j])
        print("ans",ans)
        print(sell, buy)
        return maxCount
s = Solution().maxProfit([0,8,5,7,4,7])
print(s)