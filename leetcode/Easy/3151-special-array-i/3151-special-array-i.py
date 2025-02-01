class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((nums[i] + nums[i + 1]) % 2 for i in range(len(nums) - 1))
