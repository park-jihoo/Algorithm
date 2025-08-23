class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        y2, y1, x2, x1 = -1, inf, -1, inf
        for idx in range(m):
            for jdx in range(n):
                if grid[idx][jdx] == 1:
                    if y2 < idx:
                        y2 = idx
                    if y1 > idx:
                        y1 = idx
                    if x2 < jdx:
                        x2 = jdx
                    if x1 > jdx:
                        x1 = jdx
        
        return (y2-y1+1) * (x2-x1+1)