class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cnt_row, cnt_col = [0] * m, [0] * n
        dict_mat = [0] * (m*n+1)
        for i, j in product(range(m), range(n)):
            dict_mat[mat[i][j]] = (i, j)
        for ind, num in enumerate(arr):
            i, j = dict_mat[num]
            cnt_row[i] += 1
            cnt_col[j] += 1
            if cnt_row[i] == n or cnt_col[j] == m:
                return ind
        return -1