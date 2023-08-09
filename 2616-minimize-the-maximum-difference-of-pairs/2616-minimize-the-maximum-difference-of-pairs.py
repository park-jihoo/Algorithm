class Solution:
    def countPairs(self, nums, difference):
        n = len(nums)
        idx, cnt = 0, 0
        while idx < n - 1:
            if nums[idx + 1] - nums[idx] <= difference:
                cnt += 1
                idx += 1
            idx += 1
        return cnt

    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if self.countPairs(nums, mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left
