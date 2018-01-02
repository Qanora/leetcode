class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        prices.insert(0,prices[0])
        prices.append(prices[-1])
        print(prices)
        buy = []
        sell = []
        for i in range(1,len(prices)-1):
            if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
                sell.append(prices[i])
            if prices[i-1] >= prices[i] and prices[i] < prices[i+1]:
                buy.append(prices[i])
        count = 0
        for i in range(len(sell)):
            count += sell[i] - buy[i]
        print(buy, sell)
        return count

s = Solution().maxProfit([1,2])
print(s)