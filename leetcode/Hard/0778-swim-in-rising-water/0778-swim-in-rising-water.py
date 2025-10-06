class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited, ans = set(), 0
        while q:
            h, r, c = heapq.heappop(q)
            ans = max(ans, h)
            if r == (n - 1) and c == (n - 1):
                return ans
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in d:
                if (
                    0 <= r + dr < n
                    and 0 <= c + dc < n
                    and (r + dr, c + dc) not in visited
                ):
                    heapq.heappush(q, (grid[r + dr][c + dc], r + dr, c + dc))
        return ans
