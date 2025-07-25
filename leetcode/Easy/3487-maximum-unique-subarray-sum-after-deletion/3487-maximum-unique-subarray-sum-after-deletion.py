class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return sum(set([x for x in nums if x > 0]))
