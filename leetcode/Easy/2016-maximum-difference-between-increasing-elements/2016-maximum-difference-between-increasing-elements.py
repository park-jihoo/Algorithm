class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        pref = list(accumulate(nums, min))
        return max(x-p for x, p in zip(nums, pref)) or -1