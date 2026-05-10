class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n, dp = len(nums), [float('-inf')]*len(nums)
        dp[0] = 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i]+1)
        return -1 if dp[n-1] == float('-inf') else dp[n-1]