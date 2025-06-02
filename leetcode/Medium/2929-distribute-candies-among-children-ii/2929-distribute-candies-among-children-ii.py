class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        s = 0
        for i in range(0, min(n, limit) + 1):
            s += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return s
