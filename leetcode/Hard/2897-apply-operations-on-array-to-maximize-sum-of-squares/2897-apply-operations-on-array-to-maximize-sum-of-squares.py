class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        b = [0] * 30
        ans, mod = 0, 1000000007

        # Step 1: count the 1-bits in every bit position
        for x in nums:
            for i in range(30):
                if x & (1 << i):
                    b[i] += 1

        # Step 2: build k numbers, each takes one 1-bit from every position that still has one
        for _ in range(k):
            x = 0
            for i in range(30):
                if b[i] > 0:
                    x |= 1 << i
                    b[i] -= 1
            ans = (ans + x * x) % mod

        return ans