class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        q = []
        maxval = m * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = maxval
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            row, col = q[0]
            del q[0]
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n:
                    if mat[r][c] > mat[row][col] + 1:
                        q.append((r, c))
                        mat[r][c] = mat[row][col] + 1
        return mat
