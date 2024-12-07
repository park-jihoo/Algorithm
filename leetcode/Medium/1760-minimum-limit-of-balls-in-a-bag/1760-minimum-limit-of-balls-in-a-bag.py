class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # minimize max(math.ceil(x[i] / (operations[i] + 1))) where sum(operations) = maxoperations

        return bisect_left(range(1, max(nums)+1), 0, key=lambda x : maxOperations - sum((n-1)//x for n in nums)) + 1