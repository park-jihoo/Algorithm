class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph, dist = defaultdict(list), [(i>0)*(-1) for i in range(n)]
        for u,v,w in edges: graph[u].append((w,v)); graph[v].append((2*w,u))
        queue = [(0,0)];  heapq.heapify(queue)
        while queue and queue[0][1] != n-1:
            wu,u = heapq.heappop(queue)
            if  0 <= dist[u] < wu:  continue
            for wv,v in graph[u]:
                if  dist[v] < 0  or  wu+wv < dist[v]:
                    dist[v] = wu+wv; heapq.heappush(queue, (dist[v], v))
        return dist[n-1]