class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            center = (start + end) // 2
            if nums[center] == nums[center + 1] and center % 2 == 0:
                start = center + 1
            elif nums[center] == nums[center - 1] and center % 2 == 0:
                end = center - 1
            elif nums[center] == nums[center + 1] and center % 2 == 1:
                end = center - 1
            elif nums[center] == nums[center - 1] and center % 2 == 1:
                start = center + 1
            else:
                return nums[center]
        return nums[start]