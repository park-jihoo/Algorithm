class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            bits.append(n&1)
            n = n >> 1
        ans = 0
        for i in range(32):
            ans = ans << 1
            ans += bits[i]
        return ans