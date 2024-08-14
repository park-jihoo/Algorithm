class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        self.nums = sorted(nums)
        self.k = k
        self.n = len(nums)
        
        left, right = 0, self.nums[-1] - self.nums[0]
        while left < right:
            mid = (left + right) // 2
            if self.check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, dist: int) -> bool:
        cnt = 0
        j = 0
        for i in range(self.n):
            while j < self.n and self.nums[j] - self.nums[i] <= dist:
                j += 1
            cnt += j - i - 1
        return cnt >= self.k