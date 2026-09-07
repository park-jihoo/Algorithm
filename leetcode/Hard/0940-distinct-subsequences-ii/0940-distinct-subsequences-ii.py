class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n, mod = len(s), 10**9 + 7
        dp, ans = [0] * 26, 0
        for i in range(n):
            idx = ord(s[i]) - ord("a")
            cur = (1 + ans - dp[idx] + mod) % mod
            ans = (ans + cur) % mod
            dp[idx] = (dp[idx] + cur) % mod
        return ans
