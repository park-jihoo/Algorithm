class Solution:
    def isBipartite(self, n, graph):
        color = [-1] * (n + 1)
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
        return True

    def union(self, parent, x):
        if parent[x] == x:
            return x
        return self.union(parent, parent[x])

    def bfs(self, graph, start):
        q, visited, level = deque([start]), set([start]), 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nbr in graph[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
            level += 1
        return level

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n + 1))
        graph = defaultdict(list)
        for u, v in edges:
            parent[self.union(parent, u)] = self.union(parent, v)
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, n + 1):
            parent[i] = self.union(parent, parent[i])

        m = defaultdict(list)
        for i in range(1, n + 1):
            m[parent[i]].append(i)
        ans = 0
        for nodes in m.values():
            if not self.isBipartite(n, graph):
                return -1
            ans += max(self.bfs(graph, node) for node in nodes)
        return ans
