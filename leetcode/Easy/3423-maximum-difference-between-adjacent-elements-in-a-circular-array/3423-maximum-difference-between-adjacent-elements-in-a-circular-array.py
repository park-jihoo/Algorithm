class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = abs(nums[n - 1] - nums[0])
        for i in range(n - 1):
            ans = max(ans, abs(nums[i + 1] - nums[i]))
        return ans
