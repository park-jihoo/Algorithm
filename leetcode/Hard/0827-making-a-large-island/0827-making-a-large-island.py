class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        waters = defaultdict(int)
        def dfs(x, y):
            s, water, area = [(x,y)], set(), 1
            while s:
                i, j = s.pop()
                for di, dj in [(0,1), (0, -1), (1,0), (-1,0)]:
                    if 0<=i+di<m and 0<=j+dj<n:
                        if grid[i+di][j+dj] == 1:
                            grid[i+di][j+dj] = -1
                            s.append((i+di, j+dj))
                            area += 1
                        elif grid[i+di][j+dj] == 0:
                            water.add((i+di, j+dj))
            for cell in water:
                waters[cell] += area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    dfs(i, j)
        if waters:
            return 1 + max(waters.values())
            
        return 1 if grid[0][0]==0 else m*n

