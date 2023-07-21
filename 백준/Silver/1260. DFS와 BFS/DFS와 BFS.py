n, m, v = map(int, input().split())

board = {x: [] for x in range(1, n + 1)}

for i in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)


def dfs(board, v):
    need_visited, visited = list(), list()
    need_visited.append(v)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(sorted(board[node], reverse=True))
    return visited


def bfs(board, v):
    need_visited, visited = list(), list()
    need_visited.append(v)
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(sorted(board[node]))
    return visited


print(" ".join([str(x) for x in dfs(board, v)]))
print(" ".join([str(x) for x in bfs(board, v)]))
