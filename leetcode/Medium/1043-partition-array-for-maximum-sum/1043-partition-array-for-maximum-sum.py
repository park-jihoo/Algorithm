class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)
        for i in range(1, len(arr)+1):
            cur = 0
            for j in range(1, min(k, i) +1):
                cur = max(cur, arr[i-j])
                dp[i] = max(dp[i], dp[i-j]+cur*j)
        return dp[len(arr)]