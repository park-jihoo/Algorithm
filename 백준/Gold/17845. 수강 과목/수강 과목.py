n, k = map(int, input().split())
dp = [[0] * (n + 1) for x in range(k + 1)]
times = []
imps = []

for x in range(k):
    i, t = map(int, input().split())
    times.append(t)
    imps.append(i)

for c in range(1, k + 1):
    for t in range(1, n + 1):
        if times[c - 1] > t:
            dp[c][t] = dp[c - 1][t]
        else:
            dp[c][t] = max(imps[c - 1] + dp[c - 1][t - times[c - 1]], dp[c - 1][t])

print(dp[k][n])