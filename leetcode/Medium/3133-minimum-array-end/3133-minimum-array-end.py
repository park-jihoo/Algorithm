class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans, mask = x, 1
        n -= 1
        while n > 0:
            if (mask & x) == 0:
                ans |= (n & 1) * mask
                n >>= 1
            mask <<= 1
        return ans