class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # XOR operator ^
        # XOR twice then original value
        xors = [i^k for i in nums]
        ans = sum(max(xors[i], nums[i]) for i in range(len(nums)))
        cnt = sum(xors[i] > nums[i] for i in range(len(nums)))
        if cnt % 2:
            ans -= min(abs(nums[i] - xors[i]) for i in range(len(nums)))
        return ans