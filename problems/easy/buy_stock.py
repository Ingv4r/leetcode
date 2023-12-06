class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif cur_price := (prices[i] - min_price) > profit:
                profit = prices[i] - cur_price
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
