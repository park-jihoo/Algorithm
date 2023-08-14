class Solution:
    def __init__(self):
        self.nums = []

    def findIdx(self, num):
        # binary search
        left, right = 0, len(self.nums) - 1
        if num > self.nums[right]:
            return len(self.nums)
        if num <= self.nums[0]:
            return 0
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def numSubseq(self, nums: List[int], target: int) -> int:
        self.nums = sorted(nums)
        answer = 0
        for idx, num in enumerate(self.nums):
            if target - num < num:
                break
            end = self.findIdx(target - num)
            answer += 2 ** max(0, end - idx - 1)
        return answer % (10**9 + 7)
