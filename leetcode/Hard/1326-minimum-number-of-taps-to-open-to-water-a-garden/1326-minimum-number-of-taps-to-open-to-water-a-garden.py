class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n+2]*n
        for idx, val in enumerate(ranges):
            for j in range(max(idx-val+1,0),min(idx+val,n)+1):
                dp[j] =  min(dp[j], dp[max(0, idx - val)] + 1)
        return dp[n] if dp[n] < n + 2 else -1