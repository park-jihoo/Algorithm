class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = list(accumulate(nums, max))
        
        min_idx = n - 1
        for i in range(n - 2, -1, -1):
            if ans[i] > nums[min_idx]:
                ans[i] = ans[min_idx]
            if nums[i] < nums[min_idx]:
                min_idx = i
        return ans