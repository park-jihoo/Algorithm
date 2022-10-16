class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        m = float("-inf")
        stack = []
        for i in reversed(range(len(nums))):
            if nums[i] < m:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    m = stack.pop()
                stack.append(nums[i])
        return False