class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        hor = list(accumulate(sum(x) for x in grid))
        ver = list(accumulate(sum(x[i] for x in grid) for i in range(len(grid[0]))))
        return (hor[-1] % 2 == 0 and hor[-1] // 2 in hor) or (
            ver[-1] % 2 == 0 and ver[-1] // 2 in ver
        )
