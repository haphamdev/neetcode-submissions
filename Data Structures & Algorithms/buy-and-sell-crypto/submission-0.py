class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for p in prices:
            if p < buy:
                buy = p
            else:
                currentProfit = p - buy
                profit = max(profit, currentProfit)
        return profit
