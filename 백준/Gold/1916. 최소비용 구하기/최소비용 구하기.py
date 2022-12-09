import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
dist = [int(1e9)] * (n + 1)

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue
        for node in graph[now]:
            cost = d + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(start)

print(dist[end])
