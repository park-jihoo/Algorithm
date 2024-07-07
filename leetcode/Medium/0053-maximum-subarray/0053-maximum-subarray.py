class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            ans = max(ans, nums[i])
        return ans
