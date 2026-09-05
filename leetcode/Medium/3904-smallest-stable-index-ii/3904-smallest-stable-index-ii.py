class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pmax, pmin = (
            list(accumulate(nums, max)),
            list(accumulate(nums[::-1], min))[::-1],
        )
        for i in range(len(nums)):
            if pmax[i] - pmin[i] <= k:
                return i
        return -1
