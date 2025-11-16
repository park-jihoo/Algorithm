class Solution:
    def numSub(self, s: str) -> int:
        ans, mod = 0, 10**9 + 7
        for x in s.split("0"):
            ans += (len(x) * (len(x) + 1)) // 2
            ans %= mod
        return ans
