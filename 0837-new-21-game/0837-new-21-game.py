class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        ans = 0.0
        dp = [1.0] + [0.0] * (n)
        window_sum = dp[0]

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                ans += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
        return ans
