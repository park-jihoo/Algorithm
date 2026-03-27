class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        for idx, row in enumerate(mat):
            if idx % 2:
                if mat[idx] != mat[idx][(n - k) :] + mat[idx][: (n - k)]:
                    return False
            else:
                if mat[idx] != mat[idx][k:] + mat[idx][:k]:
                    return False
        return True
