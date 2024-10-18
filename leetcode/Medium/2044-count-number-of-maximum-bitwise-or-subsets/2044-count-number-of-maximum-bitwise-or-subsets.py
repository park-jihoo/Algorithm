class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = functools.reduce(lambda a, b: a | b, nums)
        dp = [0] * (1 << 17)
        dp[0] = 1
        for num in nums:
            for i in range(maxor, -1, -1):
                dp[i | num] += dp[i]
        return dp[maxor]
