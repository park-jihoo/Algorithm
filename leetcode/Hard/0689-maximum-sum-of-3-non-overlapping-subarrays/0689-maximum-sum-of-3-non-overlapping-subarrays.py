class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums, l = [], len(nums)
        sums.append(sum(nums[:k]))
        for i in range(0, l - k):
            sums.append(sums[-1] + nums[i+k] - nums[i])

        n, d = len(sums), 3

        dp = [[-inf for _ in range(d + 1)] for _ in range(n + 1)]
        for i in range(n + 1): 
            dp[i][0] = 0


        h = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, d + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                val = dp[i - k][j - 1] if i - k >= 0 else 0
                if dp[i][j] < sums[i - 1] + val:
                    dp[i][j] = sums[i - 1] + val
                    h[dp[i][j]] = h[dp[i - k][j - 1]] + [i-1]

        return h[dp[n][d]]