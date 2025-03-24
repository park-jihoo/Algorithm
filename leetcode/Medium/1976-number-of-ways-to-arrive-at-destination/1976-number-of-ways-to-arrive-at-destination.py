class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        dist, ans = [float("inf")] * n, [0] * n
        pq = [(0, 0)]
        dist[0], ans[0] = 0, 1
        mod = 10**9 + 7
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nbr, time in graph[node]:
                if dist[node] + time < dist[nbr]:
                    dist[nbr] = dist[node] + time
                    ans[nbr] = ans[node]
                    heapq.heappush(pq, (dist[nbr], nbr))
                elif dist[node] + time == dist[nbr]:
                    ans[nbr] = (ans[nbr] + ans[node]) % mod

        return ans[n - 1]
