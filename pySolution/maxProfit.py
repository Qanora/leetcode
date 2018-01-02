class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minV, maxV = 0,0
        maxProfit = 0
        for val in range(len(prices)):
            if prices[minV] > prices[val]:
                minV = val
                prices[maxV] = prices[val]
            if prices[maxV] < prices[val]:
                maxV = val
                maxProfit = max(prices[maxV] - prices[minV], maxProfit)
        return maxProfit
s = Solution().maxProfit([2,4,1])
print(s)