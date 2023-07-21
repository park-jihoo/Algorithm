class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = 0
        notholding = float("inf")

        for price in prices:
            notholding = min(notholding, price)
            holding = max(holding, price - notholding)
        return holding
