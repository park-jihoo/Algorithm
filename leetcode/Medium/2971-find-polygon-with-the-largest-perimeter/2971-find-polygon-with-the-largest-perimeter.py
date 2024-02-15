class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) == 3 and nums[0] > nums[1] + nums[2]:
            return -1
        for idx in range(len(nums) - 2):
            if nums[idx] < sum(nums[idx + 1 :]):
                return sum(nums[idx:])
        return -1
