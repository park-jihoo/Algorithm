class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(len(s) // 2):
            if s[2 * i] != s[2 * i + 1]:
                ans += 1
        return ans
