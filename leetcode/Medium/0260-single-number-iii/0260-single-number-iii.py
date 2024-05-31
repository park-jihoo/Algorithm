class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [key for key, val in Counter(nums).items() if val == 1]