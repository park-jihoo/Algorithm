# 6 seconds in Python

from collections import deque

directions = {
    0: (-1, 0),
    1: (0, -1),
    2: (0, 1),
    3: (1, 0)
}

pipe_dict = (
    (),
    ((1, 2), (0, 3)),
    ((1, 2), (0, 3)),
    ((3, 2), (1, 3), (1, 0), (0, 2)),
    ((3, 2), (1, 3), (1, 0), (0, 2)),
    ((3, 2), (1, 3), (1, 0), (0, 2)),
    ((3, 2), (1, 3), (1, 0), (0, 2))
)

def bfs(arr, start):
    visited=set()
    if start == 0:
        q = deque([(0, 0, 1, 0, visited)])
        end = N-1
        end_dir = 2
    else:
        q = deque([(N-1, N-1, 2, 0, visited)])
        end = 0
        end_dir = 1
    ans = N * N + 1
    dij = [[[N * N] * N for _ in range(N)] for _ in range(4)]

    while q:
        y, x, dir_from, time, visited = q.popleft()
        if time >= ans:
            continue
        if time >= dij[dir_from][y][x]:
            continue
        p = arr[y][x]
        if y==end and x==end:
            for dir_to in pipe_dict[p]:
                if dir_from in dir_to and end_dir in dir_to:
                    ans = time + 1
            continue
        visited.add((y, x))
        dij[dir_from][y][x] = time

        for dir_to in pipe_dict[p]:
            if dir_from in dir_to:
                for d in dir_to:
                    if d == dir_from:
                        continue
                    dy, dx = directions[d]
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                        q.append((ny, nx, 3-d, time + 1, visited.copy()))

    return ans

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {min(bfs(arr, 0), bfs(arr, 1))}')