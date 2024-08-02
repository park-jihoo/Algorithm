class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones, n = nums.count(1), len(nums)
        x, ones_in = 0, 0
        for i in range(n * 2):
            if i >= ones and nums[i % n - ones]:
                x -= 1
            if nums[i % n] == 1:
                x += 1
            ones_in = max(x, ones_in)
        return ones - ones_in
