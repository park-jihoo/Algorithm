class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans, cur = 0, 0
        for c in reversed(s):
            if c == '0':
                ans += 1
            elif cur + (1 << ans) <= k:
                cur += (1 << ans)
                ans += 1
        return ans
