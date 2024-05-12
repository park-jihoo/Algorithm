class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(grid)
        temp = [[max(row[x-1], row[x], row[x+1]) for x in range(1, n - 1)] for row in grid]
        return [[max(temp[x-1][i], temp[x][i], temp[x+1][i]) for i in range(n-2)] for x in range(1, n-1)]
                