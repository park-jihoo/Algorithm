class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, size = 0, 0
        for r in range(len(nums)):
            while nums[r] / nums[l] > k:
                l += 1
            size = max(size, r-l+1)
        return len(nums) - size