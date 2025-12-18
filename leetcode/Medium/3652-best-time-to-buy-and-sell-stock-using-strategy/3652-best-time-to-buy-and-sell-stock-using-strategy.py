class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profit = [0] + list(accumulate(prices[i] * strategy[i] for i in range(n)))
        price = [0] + list(accumulate(prices))
        ans = profit[n]

        for i in range(k - 1, n):
            left, right = profit[i - k + 1], profit[n] - profit[i + 1]
            change = price[i + 1] - price[i - k // 2 + 1]
            ans = max(ans, left + right + change)
        return ans
