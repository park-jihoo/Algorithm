class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums)-bisect_right(nums,0), bisect_left(nums, 0))