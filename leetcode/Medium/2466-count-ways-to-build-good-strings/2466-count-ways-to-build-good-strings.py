class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        dp[zero] +=1
        dp[one] +=1
        for i in range(min(zero, one)+1, high+1):
            if i > zero:
                dp[i] += dp[i - zero]
            if i > one:
                dp[i] += dp[i - one]
        return sum(dp[low:high+1]) % (10 ** 9 + 7)