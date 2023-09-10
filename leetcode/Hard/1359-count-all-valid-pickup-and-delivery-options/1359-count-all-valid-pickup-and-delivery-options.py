class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (i*(2*i-1)*dp[i-1])%(10**9+7)
        return dp[n]