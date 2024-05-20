class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = reduce(lambda x, y:x|y, nums)
        # 00 + (01) + (11) + (01 ^ 11)
        # 00 + 01 + 11 + 10 => 11 * 2 = 110
        # 000 + 101 + 001 + 110 + 101 ^ 001 + 101 ^ 110 + 001 ^ 110 + 101 ^ 001 ^ 110
        # 000 + 101 + 001 + 110 + 100 + 011 + 111 + 010 => 111 * 4
        return ans * (2 ** (len(nums) - 1))