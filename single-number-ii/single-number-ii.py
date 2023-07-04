class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones
        return ones


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[::-1][0][0]