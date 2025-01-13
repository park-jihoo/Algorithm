class Solution:
    def minimumLength(self, s: str) -> int:
        cnt, ans = Counter(s), 0
        for key, val in cnt.items():
            if val >= 3:
                ans += 2 * ((val - 1) // 2)
        return len(s) - ans
