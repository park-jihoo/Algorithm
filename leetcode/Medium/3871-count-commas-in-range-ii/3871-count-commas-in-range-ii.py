class Solution:
    def countCommas(self, n: int) -> int:
        return sum(max(n + 1 - (10 ** (3 * x)), 0) for x in range(1, 6))
