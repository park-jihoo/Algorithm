# acmicpc 23288

from collections import deque

n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def rotate(d, x, y):
    global dice
    if d == 0:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif d == 1:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif d == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    else:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    if dice[-1] > grid[x][y]:
        return (d + 1) % 4
    elif dice[-1] < grid[x][y]:
        return (d + 3) % 4
    else:
        return d


def cal_score(score, x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = True
    tot_score = 0

    while queue:
        x, y = queue.popleft()
        tot_score += score
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == score:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return tot_score


dice = [1, 2, 3, 4, 5, 6]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_x, cur_y, cur_d, ans = 0, 0, 0, 0

for _ in range(k):
    dx, dy = directions[cur_d]
    if not (0 <= cur_x + dx < n and 0 <= cur_y + dy < m):
        cur_d = (cur_d + 2) % 4
        dx, dy = directions[cur_d]

    new_x, new_y = cur_x + dx, cur_y + dy
    cur_d = rotate(cur_d, new_x, new_y)
    ans += cal_score(grid[new_x][new_y], new_x, new_y)
    cur_x, cur_y = new_x, new_y

print(ans)