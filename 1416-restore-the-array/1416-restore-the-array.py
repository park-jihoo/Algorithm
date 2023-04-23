class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # Too many hard... String and DP
        n = len(s)
        klen = len(str(k))

        dp = [0] * (klen+1)
        dp[n%len(dp)] = 1
        for i in reversed(range(len(s))):
            dp[i%len(dp)] = 0
            if s[i] == '0':
                continue
            curr = 0
            for j in range(i, min(i+klen, n)):
                curr = 10*curr + int(s[j])
                if curr > k:
                    break
                dp[i%len(dp)] = (dp[i%len(dp)]+dp[(j+1)%len(dp)])%(10**9+7)
        return dp[0]
