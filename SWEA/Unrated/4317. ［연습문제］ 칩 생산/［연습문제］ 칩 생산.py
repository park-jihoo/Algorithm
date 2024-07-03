t = int(input())


def check(x, y):
    if 0 <= x < h - 1 and 0 <= y < w - 1:
        if (
            arr[x][y] == 0
            and arr[x + 1][y] == 0
            and arr[x][y + 1] == 0
            and arr[x + 1][y + 1] == 0
        ):
            return True
    return False


def dfs(x, y, cnt):
    global ans
    if x >= h - 1:
        x = 0
        y += 1
    if y >= w - 1:
        ans = max(ans, cnt)
        return
    if x == 0:
        bit = 0
        for i in range(h):
            bit |= arr[i][y] << i
        if dp[bit][y] >= cnt:
            return
        dp[bit][y] = cnt
    if check(x, y):
        arr[x][y] = arr[x + 1][y] = arr[x][y + 1] = arr[x + 1][y + 1] = 1
        dfs(x + 2, y, cnt + 1)
        arr[x][y] = arr[x + 1][y] = arr[x][y + 1] = arr[x + 1][y + 1] = 0
    dfs(x + 1, y, cnt)


for test_case in range(1, t + 1):
    h, w = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    dp = [[-1] * w for _ in range(1 << h)]
    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")
