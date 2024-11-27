class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        def bfs(start: int, end: int) -> int:
            visited = [-1] * n
            queue = deque([(start, 0)])
            visited[start] = 0

            while queue:
                node, dist = queue.popleft()
                if node == end:
                    return dist
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))
            return float("inf")

        ans = []
        for s, e in queries:
            if e not in graph[s]:
                graph[s].append(e)

            ans.append(bfs(0, n - 1))

        return ans
