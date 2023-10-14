class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[n][i] = float("inf")

        for i in range(n - 1, -1, -1):
            for r in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, r - 1 - time[i])]
                dont = dp[i + 1][r]
                dp[i][r] = min(paint, dont)
        return dp[0][n]
