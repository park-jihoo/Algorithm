class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [10**10] * (len(nums) + 1)
        for val in nums:
            dp[bisect.bisect_left(dp, val)] = val
        return dp.index(10**10)

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1, n - 1):
            left = [num for num in nums[:i] if num < nums[i]] + [nums[i]]
            right = [nums[i]] + [num for num in nums[i + 1 :] if num < nums[i]]
            right = right[::-1]
            a, b = self.lengthOfLIS(left), self.lengthOfLIS(right)
            if a >= 2 and b >= 2:
                ans = max(ans, a + b - 1)

        return n - ans
