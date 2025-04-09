class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1
        distinct = {num for num in nums if num > k}
        return len(distinct)
