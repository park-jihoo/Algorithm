n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def mul(x, y):
    k = len(x)
    z = [[0] * k for _ in range(k)]

    for r in range(k):
        for c in range(k):
            e = 0
            for i in range(k):
                e += x[r][i] * y[i][c]
            z[r][c] = e % 1000
    return z


def square(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= 1000
        return a
    tmp = square(a, b // 2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)


result = square(a, b)

for i in result:
    print(*i)
