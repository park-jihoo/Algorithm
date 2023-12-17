class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = [sum(x) for x in grid]
        onesCol = [
            sum([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))
        ]

        return [
            [
                2 * (onesRow[j] + onesCol[i]) - (len(grid[0]) + len(grid))
                for i in range(len(grid[0]))
            ]
            for j in range(len(grid))
        ]
