class Solution:
    def count(self, val, digit, suf):
        sval = str(val)
        prflen = len(sval) - len(suf)
        if prflen < 0:
            return 0
        dp = [[0] * 2 for _ in range(prflen + 1)]
        dp[prflen][0] = 1
        dp[prflen][1] = 1 if sval[prflen:] >= suf else 0
        for i in range(prflen - 1, -1, -1):
            curr = int(sval[i])
            dp[i][0] = (digit + 1) * dp[i + 1][0]
            dp[i][1] = (
                (curr * dp[i + 1][0] + dp[i + 1][1])
                if curr <= digit
                else (digit + 1) * dp[i + 1][0]
            )
        return dp[0][1]

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # digit dp
        return self.count(finish, limit, s) - self.count(start - 1, limit, s)
