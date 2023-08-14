import sys

sys.setrecursionlimit(10**6)

scc = [0] * 10010
p = []

v, e = map(int, input().split())
s = 0

graph = {x: [] for x in range(v + 1)}
grapht = {x: [] for x in range(v + 1)}
visited = [False for _ in range(v + 1)]


def dfs(x):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node)
    p.append(x)


def dfs2(k, x):
    visited[x] = True
    scc[x] = k
    for node in grapht[x]:
        if not visited[node]:
            dfs2(k, node)


for i in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    grapht[end].append(start)

for i in range(1, v + 1):
    if not visited[i]:
        dfs(i)

visited = [False] * (v + 1)

while p:
    c = p.pop()
    if visited[c]:
        continue
    s += 1
    dfs2(s, c)

print(s)
for i in range(1, v + 1):
    if scc[i] == -1:
        continue
    print(i, end=" ")
    for j in range(i + 1, v + 1):
        if scc[j] == scc[i]:
            print(j, end=" ")
            scc[j] = -1
    print(-1)
