class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans = max(s[:i].count("0") + s[i:].count("1"), ans)
        return ans
