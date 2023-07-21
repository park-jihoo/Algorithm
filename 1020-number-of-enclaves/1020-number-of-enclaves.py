from collections import deque


class Solution:
    def __init__(self):
        self.visited = set()
        self.enclave = 0
        self.m = 0
        self.n = 0
        self.grid = []

    def dfs1(self, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return 0
        if self.grid[i][j] == 0 or (i, j) in self.visited:
            return 1
        self.visited.add((i, j))
        t = self.dfs1(i + 1, j)
        b = self.dfs1(i - 1, j)
        l = self.dfs1(i, j - 1)
        r = self.dfs1(i, j + 1)
        return t and b and l and r

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        visit = set()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    if self.dfs1(i, j):
                        self.enclave += len(self.visited)
                        print(self.visited)
                    visit.update(self.visited)
                    self.visited = set()
        return self.enclave
        answer = 0
