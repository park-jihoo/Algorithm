import sys

sys.setrecursionlimit(10**6)

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

visited[0][0] = 1


def dfs(r, c):
    global count
    global board
    global visited
    now = board[r][c]
    if r == 0 and c == 0:
        return 1
    if visited[r][c] == -1:
        visited[r][c] += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] > now:
                visited[r][c] += dfs(nr, nc)
    return visited[r][c]


result = dfs(m - 1, n - 1)
print(result)
