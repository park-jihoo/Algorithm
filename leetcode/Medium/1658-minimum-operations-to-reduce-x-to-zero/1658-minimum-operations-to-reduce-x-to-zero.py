class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        n = len(nums)
        goal = s - x
        maxlen = -1
        left = 0
        cursum = 0
        for right, num in enumerate(nums):
            cursum += num
            while cursum > goal and left <= right:
                cursum -= nums[left]
                left += 1
            if cursum == goal:
                maxlen = max(maxlen, right - left + 1)
        return n - maxlen if maxlen != -1 else -1