class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        mx = [0] * n
        mn = [0] * n

        mx[0] = mn[0] = grid[0][0]
        for j in range(1, n):
            mx[j] = mn[j] = mx[j - 1] * grid[0][j]

        for i in range(1, m):
            mx[0] = mn[0] = mx[0] * grid[i][0]

            for j in range(1, n):
                x = grid[i][j]

                a = mx[j] * x
                b = mn[j] * x
                c = mx[j - 1] * x
                d = mn[j - 1] * x

                mx[j] = max(a, b, c, d)
                mn[j] = min(a, b, c, d)

        ans = mx[-1]
        return -1 if ans < 0 else ans % MOD
