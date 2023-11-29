class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(x) for x in list(bin(n)[2:])])
