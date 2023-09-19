from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
visited[R] = 1

queue = deque([R])

cnt = 1
while queue:
    node = queue.popleft()
    graph[node].sort()

    for i in graph[node]:
        if not visited[i]:
            queue.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)
