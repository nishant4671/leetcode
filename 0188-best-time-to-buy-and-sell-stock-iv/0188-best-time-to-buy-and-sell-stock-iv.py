class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        dp0 = [0] * (k + 1)
        dp1 = [-10**9] * (k + 1)
        for price in prices:
            for t in range(1, k + 1):
                dp0[t] = max(dp0[t], dp1[t] + price)
                dp1[t] = max(dp1[t], dp0[t - 1] - price)
        return dp0[k]