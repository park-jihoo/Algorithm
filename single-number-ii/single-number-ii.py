class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[::-1][0][0]