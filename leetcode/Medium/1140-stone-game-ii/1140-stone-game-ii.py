class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # DP, Array, Math, Game Theory

        n = len(piles)

        if n == 0:
            return 0

        sums = [0] * n
        for i in reversed(range(n)):
            sums[i] = piles[i]
            if i + 1 < n:
                sums[i] += sums[i + 1]

        dp = {}

        for m in range(1, 2 * n + 1):
            dp[(n, m)] = 0

        for k in reversed(range(n)):
            for m in reversed(range(n + 1)):
                dp[(k, m)] = 0
                for x in range(1, 2 * m + 1):
                    if k + x <= n:
                        dp[(k, m)] = max(dp[(k, m)], sums[k] - dp[(k + x, max(x, m))])

        return dp[(0, 1)]
