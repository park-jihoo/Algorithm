class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n, ans, total = len(arr), len(arr) + 1, 0
        dp = [n] * (n + 1)
        left = 0
        for right, x in enumerate(arr):
            total += x
            while total > target:
                total -= arr[left]
                left += 1
            dp[right + 1] = dp[right]
            if total == target:
                ans = min(ans, right - left + 1 + dp[left])
                dp[right + 1] = min(dp[right], right - left + 1)
        return -1 if ans == n + 1 else ans