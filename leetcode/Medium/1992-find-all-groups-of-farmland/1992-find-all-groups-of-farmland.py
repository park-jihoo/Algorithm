class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(land), len(land[0])

        for i in range(m):
            for j in range(n):
                if (
                    land[i][j] == 1
                    and (i == 0 or land[i - 1][j] == 0)
                    and (j == 0 or land[i][j - 1] == 0)
                ):
                    bottom_row = i
                    right_col = j

                    while bottom_row + 1 < m and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    while right_col + 1 < n and land[i][right_col + 1] == 1:
                        right_col += 1
                    ans.append([i, j, bottom_row, right_col])

        return ans
