class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        mod = 10**9 + 7
        dp[1] = 1
        window = 0
        for i in range(2, n + 1):
            enter, out = i - delay, i - forget
            if enter >= 1:
                window = (window + dp[enter]) % mod
            if out >= 1:
                window = (window - dp[out] + mod) % mod
            dp[i] = window
        start = max(1, n - forget + 1)
        return sum(dp[start : n + 1]) % mod
