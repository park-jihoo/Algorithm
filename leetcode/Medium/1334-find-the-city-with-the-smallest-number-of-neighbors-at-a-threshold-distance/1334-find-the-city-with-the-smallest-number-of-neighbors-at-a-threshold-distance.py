class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:
        dist = [[float("inf")] * n for i in range(n)]
        for s, e, w in edges:
            dist[s][e] = w
            dist[e][s] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        over = min(
            [
                len([x for idx, x in enumerate(dist[i]) if x <= t and i != idx])
                for i in range(n)
            ]
        )
        for i in range(n - 1, -1, -1):
            if len([x for idx, x in enumerate(dist[i]) if x <= t and i != idx]) == over:
                return i
        return 0
