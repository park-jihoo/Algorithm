class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # arrays dp matrix
        n = len(grid)
        if n == 1:
            return grid[0][0]
        temp = [(val, idx) for idx, val in enumerate(grid[0])]
        dp1 = [x for x in grid[0]]
        dp2 = [0] * n
        for curr in range(1, n):
            a1, a2 = heapq.nsmallest(2, [(val, idx) for idx, val in enumerate(dp1)])
            for idx, val in enumerate(grid[curr]):
                if idx == a1[1]:
                    dp2[idx] = val + dp1[a2[1]]
                else:
                    dp2[idx] = val + dp1[a1[1]]
            dp1, dp2 = dp2, [0] * n
        return min(dp1)
