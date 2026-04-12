class Solution:
    def minimumDistance(self, word: str) -> int:
        from functools import lru_cache

        def dist(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        @lru_cache(None)
        def solve(i, f1, f2):
            if i == len(word):
                return 0

            cur = ord(word[i]) - ord("A")

            move1 = dist(f1, cur) + solve(i + 1, cur, f2)
            move2 = dist(f2, cur) + solve(i + 1, f1, cur)

            return min(move1, move2)

        return solve(0, 26, 26)
