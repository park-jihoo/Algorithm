class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for coin in range(k + 1):
                cur = 0
                for idx in range(min(coin, len(piles[i - 1])) + 1):
                    if idx > 0:
                        cur += piles[i - 1][idx - 1]
                    dp[i][coin] = max(dp[i][coin], dp[i - 1][coin - idx] + cur)
        return dp[n][k]
