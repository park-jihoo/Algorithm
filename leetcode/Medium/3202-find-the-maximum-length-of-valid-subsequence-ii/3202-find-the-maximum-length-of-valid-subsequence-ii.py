class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp, ans = [[0] * k for _ in range(k)], 0
        for num in nums:
            num %= k
            for p in range(k):
                dp[p][num] = dp[num][p] + 1
                ans = max(dp[p][num], ans)
        return ans
