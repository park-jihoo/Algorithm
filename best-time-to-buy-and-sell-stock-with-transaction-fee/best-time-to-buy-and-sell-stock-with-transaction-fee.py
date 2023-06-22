class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #DP
        holding = [0 for i in range(len(prices))]
        notholding = [0 for i in range(len(prices))]
        holding[0] = - prices[0] - fee

        for i in range(1, len(prices)):
            holding[i] = max(holding[i-1], notholding[i-1] - prices[i] - fee)
            notholding[i] = max(notholding[i-1], holding[i-1] + prices[i])

        return notholding[-1]