from collections import defaultdict, deque
from itertools import combinations

n = int(input())
pop = list(map(int, input().split()))
graph = defaultdict(list)
answer = int(1e9)


def bfs(com):
    start = com[0]
    q = deque([start])
    visited = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += pop[v]
        for u in graph[v]:
            if u not in visited and u in com:
                q.append(u)
                visited.add(u)
    return _sum, len(visited)


for i in range(n):
    _input = list(map(int, input().split()))
    for j in range(1, _input[0] + 1):
        graph[i].append(_input[j] - 1)

for i in range(1, n // 2 + 1):
    com = list(combinations(range(n), i))
    for c in com:
        sum1, v1 = bfs(c)
        sum2, v2 = bfs([i for i in range(n) if i not in c])
        if v1 + v2 == n:
            answer = min(answer, abs(sum1 - sum2))

if answer != int(1e9):
    print(answer)
else:
    print(-1)
