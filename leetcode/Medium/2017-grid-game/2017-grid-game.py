class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pref = [list(accumulate(grid[0])), list(accumulate(grid[1]))]
        ans = float('inf')
        for i in range(n):
            top = 0 if i == n-1 else (pref[0][n-1] - pref[0][i])
            bottom = 0 if i == 0 else pref[1][i-1]
            ans = min(ans, max(top, bottom))
        return ans