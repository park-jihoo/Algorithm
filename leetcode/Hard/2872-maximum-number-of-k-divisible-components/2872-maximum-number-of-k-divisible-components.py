class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n <= 1:
            return 1
        graph, ans = defaultdict(set), 0
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
        q = deque(k for k, v in graph.items() if len(v) == 1)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                c = next(iter(graph[node])) if graph[node] else -1
                if c >= 0:
                    graph[c].remove(node)
                if values[node]%k == 0:
                    ans += 1
                else:
                    values[c] += values[node]
                if c >= 0 and len(graph[c]) == 1:
                    q.append(c)
        return ans