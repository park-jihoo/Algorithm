class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # DP
        # Left, Right, Stay
        arrLen = min(arrLen, steps)
        dp = [0] * arrLen
        prevDp = [0] * arrLen
        prevDp[0] = 1
        for r in range(1, steps + 1):
            dp = [0] * arrLen
            for c in range(arrLen - 1, -1 ,-1):
                ans = prevDp[c]
                if c>0:
                    ans = (ans + prevDp[c-1])%(10**9+7)
                if c<arrLen - 1:
                    ans = (ans + prevDp[c+1])%(10**9+7)
                dp[c] = ans
            prevDp = dp
        return dp[0]