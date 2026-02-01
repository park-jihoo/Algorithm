class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        smallest = sorted(nums)[:3]
        if nums[0] in smallest:
            return sum(smallest)
        return nums[0] + sum(smallest[:2])