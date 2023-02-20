class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            center = (start + end) // 2
            if nums[center] > target:
                end = center - 1
            elif nums[center] < target:
                start = center + 1
            else:
                return center
        return start
                
        