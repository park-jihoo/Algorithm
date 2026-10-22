class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        asc = dsc = 1

        for i in range(1, n):
            asc += nums[i] == (nums[i - 1] + 1) % n
            dsc += nums[i - 1] == (nums[i] + 1) % n

        if asc == n:
            return 0 if not nums[0] else min(n - nums[0], nums[0] + 2)

        if dsc == n:
            return min(n - nums[-1], nums[-1]) + 1

        return -1
