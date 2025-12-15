class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        period, cur, n = [], 1, len(prices)
        for i in range(n - 1):
            if prices[i] - prices[i + 1] != 1:
                period.append(cur * (cur + 1) // 2)
                cur = 1
            else:
                cur += 1
        period.append(cur * (cur + 1) // 2)
        return sum(period)
