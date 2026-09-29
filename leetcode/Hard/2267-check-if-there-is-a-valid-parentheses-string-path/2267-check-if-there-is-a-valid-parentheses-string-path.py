class Solution:
    def hasValidPath(self, A: list[list[str]]) -> bool:
        m, n = len(A), len(A[0])

        if ~(m + n) & 1 or A[0][0] == ")" or A[-1][-1] == "(":
            return False

        @cache
        def dfs(i, j, x):
            x += 1 - ((ord(A[i][j]) & 1) << 1)

            if x < 0 or x > (m + n - 1) - (i + j):
                return False

            if i == m - 1 and j == n - 1:
                return x == 0

            return (i < m - 1 and dfs(i + 1, j, x)) or \
                   (j < n - 1 and dfs(i, j + 1, x))

        return dfs(0, 0, 0)
        