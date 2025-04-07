class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, odd = divmod(sum(nums), 2)
        if odd:
            return False
        bit = 1
        for num in nums:
            bit |= bit << num
        return bool(bit & (1 << target))