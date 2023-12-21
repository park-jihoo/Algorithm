class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in range(len(nums)):
            if original not in nums:
                return original
            original *=2
        return original