n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queries = list(map(int, input().split()))
dice = [0 for _ in range(6)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    query = queries[i] - 1
    nx = x + dx[query]
    ny = y + dy[query]

    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if query == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif query == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif query == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    else:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])
