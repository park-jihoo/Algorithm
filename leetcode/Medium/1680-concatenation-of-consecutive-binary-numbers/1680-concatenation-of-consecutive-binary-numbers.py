class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return n
        return (n + (self.concatenatedBinary(n - 1) << n.bit_length())) % (10**9 + 7)
