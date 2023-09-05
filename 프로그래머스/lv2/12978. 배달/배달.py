import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        cdist, cdest = heapq.heappop(queue)
        if distances[cdest] < cdist:
            continue
        for newdes, newdis in graph[cdest].items():
            distance = cdist + newdis
            if distance < distances[newdes]:
                distances[newdes] = distance
                heapq.heappush(queue, [distance, newdes])
    return distances


def solution(N, road, K):
    answer = 0
    graph = {x + 1: {y + 1: float("inf") for y in range(N)} for x in range(N)}
    for r in road:
        graph[r[0]][r[1]] = min(r[2], graph[r[0]][r[1]])
        graph[r[1]][r[0]] = min(r[2], graph[r[1]][r[0]])
    result = dijkstra(graph, 1)
    return len([x for x, y in result.items() if y <= K])
