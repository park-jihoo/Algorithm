class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for idx, val in enumerate(nums):
            ans[idx], j = 1, idx-1
            while j >= 0 and nums[j] | val != nums[j]:
                ans[j] = idx - j + 1
                nums[j] |= val
                j -= 1
        return ans
