class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0
        dp = [[0] * (target + 1) for _ in range(2)]
        mod = 10**9 + 7
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i % 2] = [0] * (target + 1)
            for j in range(i, min(i * k, target) + 1):
                dp[i % 2][j] = sum(
                    dp[(i - 1) % 2][max(0, j - t)] for t in range(1, min(k, j) + 1)
                )
                dp[i % 2][j] %= mod

        return dp[n % 2][target] % mod
