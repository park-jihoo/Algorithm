class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9+7
        m,n=len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i-1][j] == 0:
                        dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                    else:
                        dp[i][j][0] = dp[i-1][j][1]
                    dp[i][j][0] %= mod
                if j > 0:
                    if grid[i][j-1] == 0:
                        dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]
                    else:
                        dp[i][j][1] = dp[i][j-1][0]
                    dp[i][j][1] %= mod
        return sum(dp[m-1][n-1]) % mod
