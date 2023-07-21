from collections import deque


class Solution:
    def __init__(self):
        self.visited = set()
        self.island = 0
        self.m = 0
        self.n = 0
        self.grid = []

    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return 0
        if self.grid[i][j] == 1 or (i, j) in self.visited:
            return 1
        self.visited.add((i, j))
        t = self.dfs(i + 1, j)
        b = self.dfs(i - 1, j)
        l = self.dfs(i, j - 1)
        r = self.dfs(i, j + 1)
        return t and b and l and r

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0 and (i, j) not in self.visited:
                    check = self.dfs(i, j)
                    self.island += check
        return self.island
