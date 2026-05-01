class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        f, a = 0, 0
        for i in range(n):
            a += nums[i]
            f += i*nums[i]
        ans = f
        for i in range(1, n):
            f += a - n*nums[-i]
            ans = max(ans, f)
        return ans
        
