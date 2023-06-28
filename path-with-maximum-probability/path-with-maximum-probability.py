class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(dict)
        for [s, e], prob in zip(edges, succProb):
            graph[s][e] = prob
            graph[e][s] = prob
        
        dist = {node: 0 for node in range(n)}
        dist[start] = 1
        q = []
        heapq.heappush(q, [-dist[start], start])

        #dijkstra
        while q:
            curr_dist, curr_dest = heapq.heappop(q)
            curr_dist = - curr_dist
            if dist[curr_dest] < curr_dist:
                continue
            for new_dest, new_dist in graph[curr_dest].items():
                distance = curr_dist * new_dist
                if distance > dist[new_dest]:
                    dist[new_dest] = distance
                    heapq.heappush(q, [-distance, new_dest])
        return dist[end]