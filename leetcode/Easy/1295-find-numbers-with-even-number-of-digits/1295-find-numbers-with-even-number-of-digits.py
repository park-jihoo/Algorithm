class Solution:
    def evenDigit(self, x: int):
        return math.ceil(math.log10(x)) % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(self.evenDigit, nums)))