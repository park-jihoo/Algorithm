class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i, cumand, ans = 0, 0, 0
        for idx, num in enumerate(nums):
            while cumand & num != 0:
                cumand -= nums[i]
                i += 1
            cumand += num
            ans = max(ans, idx - i + 1)
        return ans
