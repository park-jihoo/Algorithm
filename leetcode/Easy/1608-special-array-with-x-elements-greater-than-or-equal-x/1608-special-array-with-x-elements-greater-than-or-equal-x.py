class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= nums[0]:
            return len(nums)
        for idx in range(1, len(nums)):
            if len(nums) - idx <= nums[idx] and len(nums) - idx > nums[idx-1]:
                return len(nums) - idx
        return -1