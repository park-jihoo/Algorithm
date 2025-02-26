class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pref = [0] + list(accumulate(nums))
        return max(pref) - min(pref)
