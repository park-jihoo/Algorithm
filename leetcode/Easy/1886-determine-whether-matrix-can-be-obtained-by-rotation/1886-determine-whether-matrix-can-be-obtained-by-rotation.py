class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)

            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for i in range(n):
                mat[i].reverse()

        for i in range(4):
            rotate(mat)
            if mat == target:
                return True

        return False