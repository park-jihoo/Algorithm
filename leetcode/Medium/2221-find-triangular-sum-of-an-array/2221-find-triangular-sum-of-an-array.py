class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(math.comb(n - 1, idx) * val for idx, val in enumerate(nums)) % 10
