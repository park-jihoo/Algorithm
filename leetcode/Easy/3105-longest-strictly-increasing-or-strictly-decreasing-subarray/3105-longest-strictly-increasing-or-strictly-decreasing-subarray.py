class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = inc_len = dec_len = 1
        for a, b in pairwise(nums):
            inc_len = inc_len + 1 if a < b else 1
            dec_len = dec_len + 1 if a > b else 1
            max_len = max(max_len, inc_len, dec_len)
        return max_len
