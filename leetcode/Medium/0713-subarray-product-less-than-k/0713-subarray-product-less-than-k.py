class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        for start in range(len(nums)):
            prod = 1
            flag = True
            for end in range(start, len(nums)):
                prod *= nums[end]
                if prod >= k:
                    break
            if prod < k:
                ans += (end - start + 1)
            else:
                ans += (end - start)
        return ans