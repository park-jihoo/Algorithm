class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for idx, val in enumerate(nums):
            if n % (idx + 1) == 0:
                ans += val * val
        return ans
