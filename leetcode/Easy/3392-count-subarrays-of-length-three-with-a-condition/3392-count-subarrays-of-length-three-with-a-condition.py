class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(int(nums[i] == (nums[i-1] + nums[i+1])*2) for i in range(1, len(nums)-1))