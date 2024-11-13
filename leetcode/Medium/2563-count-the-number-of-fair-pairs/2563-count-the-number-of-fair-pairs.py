class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            a = bisect_left(nums, lower - v, lo=0, hi=i)
            b = bisect_right(nums, upper - v, lo=0, hi=i)
            ans += b - a
        return ans
