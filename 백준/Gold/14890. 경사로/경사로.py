# acmicpc 14890

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

slope = [[0] * n for _ in range(n)]
answer = 0


def check(x, y, flag):
    height = [0] * (n + 1)
    visited = [False] * (n + 1)

    for i in range(n):
        height[i] = board[x][i] if not flag else board[i][y]

    for i in range(n - 1):
        if height[i] == height[i + 1]:
            continue
        if abs(height[i] - height[i + 1]) > 1:
            return False

        if height[i] > height[i + 1]:
            temp = height[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n and height[j] == temp and not visited[j]:
                    visited[j] = True
                else:
                    return False
        else:
            temp = height[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n and height[j] == temp and not visited[j]:
                    visited[j] = True
                else:
                    return False
    return True


for i in range(n):
    answer += check(i, 0, 0)
    answer += check(0, i, 1)

print(answer)