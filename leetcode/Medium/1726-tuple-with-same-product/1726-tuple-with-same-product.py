class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cntr = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cntr[nums[i] * nums[j]] += 1
        return sum(cntr[key] * (cntr[key] - 1) * 4 for key in cntr)
