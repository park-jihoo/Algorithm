class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(map(lambda x: x * x, nums))
        return sum(sq[len(nums) // 2 :]) - sum(sq[: len(nums) // 2])
