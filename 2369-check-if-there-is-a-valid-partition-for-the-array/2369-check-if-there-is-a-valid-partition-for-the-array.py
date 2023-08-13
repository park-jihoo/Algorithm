class Solution:
    def valid(self, nums):
        if len(nums) == 2 and nums[0] == nums[1]:
            return True
        elif len(nums) == 3:
            if nums[0] == nums[1] and nums[1] == nums[2]:
                return True
            elif nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]:
                return True
        return False

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for end in range(1, n + 1):
            for start in range(end - 3, end):
                if start < 0:
                    continue
                if dp[start] and self.valid(nums[start:end]):
                    dp[end] = True
                    break

        return dp[n]
