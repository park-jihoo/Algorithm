class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    row = mat[i]
                    col = [mat[x][j] for x in range(len(mat))]
                    if sum(row) == sum(col) and sum(row) == 1:
                        ans += 1
        return ans
