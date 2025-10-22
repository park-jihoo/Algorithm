class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            lo, hi = bisect_left(nums, nums[i] - k, 0, i), bisect_right(nums, nums[i] + k, j, n)
            ans = max(ans, min((hi - j) + (i - lo), numOperations) + j - i)
            i = j

        l, r = 0, 0
        while l < n:
            if r < n and nums[r] - nums[l] <= 2*k:
                r += 1
                ans = max(ans, min(r - l, numOperations))
            else:
                l += 1
        
        return ans