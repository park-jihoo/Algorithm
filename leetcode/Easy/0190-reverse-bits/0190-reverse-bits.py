class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)

    def reverseBits3(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans

    def reverseBits2(self, n: int) -> int:
        bits = []
        for i in range(32):
            bits.append(n & 1)
            n = n >> 1
        ans = 0
        for i in range(32):
            ans = ans << 1
            ans += bits[i]
        return ans
