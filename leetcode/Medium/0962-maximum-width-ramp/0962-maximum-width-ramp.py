class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_distance = 0

        for idx, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(idx)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                idx = stack.pop()
                max_distance = max(max_distance, j - idx)

        return max_distance
