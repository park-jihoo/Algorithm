class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1]* 5
        for i in range(1, n):
            a, e, i, o, u = dp
            dp[0] = (e+u+i)%(10**9+7)
            dp[1] = (a+i)%(10**9+7)
            dp[2] = (e+o)%(10**9+7)
            dp[3] = (i)%(10**9+7)
            dp[4] = (i+o)%(10**9+7)
        return sum(dp)%(10**9+7)