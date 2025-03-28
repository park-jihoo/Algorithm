class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # biggest island including top-left, size which is bigger than x
        m, n = len(grid), len(grid[0])
        queries_sorted = sorted((query, idx) for idx, query in enumerate(queries))
        ans = [0] * len(queries)
        heap, visited, total = [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for query, index in queries_sorted:
            while heap and heap[0][0] < query:
                v, r, c = heapq.heappop(heap)
                total += 1
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            ans[index] = total
        return ans
