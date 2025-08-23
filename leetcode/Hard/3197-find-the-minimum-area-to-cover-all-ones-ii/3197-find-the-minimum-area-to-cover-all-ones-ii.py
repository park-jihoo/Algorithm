class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        def area(points):
            if not points:
                return 0
            r1 = min(i for i, j in points)
            r2 = max(i for i, j in points)
            c1 = min(j for i, j in points)
            c2 = max(j for i, j in points)
            return (r2 - r1 + 1) * (c2 - c1 + 1)

        best = inf

        # Case 1: vertical 3 slices
        for c1 in range(n - 2):
            for c2 in range(c1 + 1, n - 1):
                left = [(i, j) for i, j in ones if j <= c1]
                mid = [(i, j) for i, j in ones if c1 < j <= c2]
                right = [(i, j) for i, j in ones if j > c2]
                if left and mid and right:
                    best = min(best, area(left) + area(mid) + area(right))

        # Case 2: horizontal 3 slices
        for r1 in range(m - 2):
            for r2 in range(r1 + 1, m - 1):
                top = [(i, j) for i, j in ones if i <= r1]
                mid = [(i, j) for i, j in ones if r1 < i <= r2]
                bot = [(i, j) for i, j in ones if i > r2]
                if top and mid and bot:
                    best = min(best, area(top) + area(mid) + area(bot))

        # Case 3: horizontal cut, then vertical split
        for r in range(m - 1):
            top = [(i, j) for i, j in ones if i <= r]
            bot = [(i, j) for i, j in ones if i > r]
            if not top or not bot:
                continue

            for c in range(n - 1):
                left = [(i, j) for i, j in bot if j <= c]
                right = [(i, j) for i, j in bot if j > c]
                if left and right:
                    best = min(best, area(top) + area(left) + area(right))

                left = [(i, j) for i, j in top if j <= c]
                right = [(i, j) for i, j in top if j > c]
                if left and right:
                    best = min(best, area(bot) + area(left) + area(right))

        # Case 4: vertical cut, then horizontal split
        for c in range(n - 1):
            left = [(i, j) for i, j in ones if j <= c]
            right = [(i, j) for i, j in ones if j > c]
            if not left or not right:
                continue

            for r in range(m - 1):
                top = [(i, j) for i, j in left if i <= r]
                bot = [(i, j) for i, j in left if i > r]
                if top and bot:
                    best = min(best, area(right) + area(top) + area(bot))

                top = [(i, j) for i, j in right if i <= r]
                bot = [(i, j) for i, j in right if i > r]
                if top and bot:
                    best = min(best, area(left) + area(top) + area(bot))

        return best
