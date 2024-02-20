class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx, val in enumerate(nums):
            if idx != val:
                return idx
        return len(nums)