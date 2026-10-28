class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                reachable = dp[j] | (dp[j - 1] if j > 0 else set())

                dp[j] = {k ^ value for k in reachable}

        return min(dp[-1])