### 2018-02-04 solved ###
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # DP
        # length = len(prices)
        # sell = [0 for i in range(length + 1 )]   # 在i位置处于卖出状态获得的最大收益
        # buy = [-60000 for i in range(length + 1)]  # 在i位置处于买入状态获得的最大收益
        # profit = 0
        # for i in range(1,length+1):
        #     sell[i] = max(buy[i-1] + prices[i-1]-fee,sell[i-1])
        #     buy[i] = max(sell[i-1] - prices[i-1],buy[i-1])
        # return sell[length]

        # DP 空间优化
        sell = 0
        buy = -prices[0]
        for price in prices:
            tmp = sell
            sell = max(buy + price - fee, sell)
            buy = max(tmp - price, buy)
        return sell
