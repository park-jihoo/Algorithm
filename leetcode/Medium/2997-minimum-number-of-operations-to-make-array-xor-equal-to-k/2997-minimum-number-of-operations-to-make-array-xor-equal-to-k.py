class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = reduce(lambda a, b: a^b, nums)
        return reduce(lambda a, b: int(a)+int(b),bin(xor^k)[2:],0)