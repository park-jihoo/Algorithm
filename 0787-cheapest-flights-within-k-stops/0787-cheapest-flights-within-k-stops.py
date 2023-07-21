from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for start, end, distance in flights:
            graph[start].append([end, distance])
        heap = [(0, src, 0)]
        K = 0
        visit = {}
        while heap:
            cost, city, K = heapq.heappop(heap)
            if city == dst:
                return cost
            if city not in visit or visit[city] > K:
                visit[city] = K
                for ci, co in graph[city]:
                    if K <= k:
                        heapq.heappush(heap, (cost + co, ci, K + 1))
        return -1
