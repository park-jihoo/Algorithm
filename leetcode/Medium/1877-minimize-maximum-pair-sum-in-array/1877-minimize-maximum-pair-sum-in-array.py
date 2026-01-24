class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums.sort()
        pairs = [nums[x]+nums[2*n - x - 1] for x in range(n)]
        return max(pairs)