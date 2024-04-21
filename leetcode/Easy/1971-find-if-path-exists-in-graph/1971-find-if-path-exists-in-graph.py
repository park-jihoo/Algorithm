class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        visited = set()
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False
