class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return 0
        
        nums.sort()
        return min(nums[n-1] - nums[2], nums[n-3] - nums[0], nums[n-2] - nums[1])
