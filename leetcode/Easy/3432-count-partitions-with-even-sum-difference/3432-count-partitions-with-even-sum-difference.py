class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return ((sum(nums) + 1) % 2 ) * (len(nums) - 1)