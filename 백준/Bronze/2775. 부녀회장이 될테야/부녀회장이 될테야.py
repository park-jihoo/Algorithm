T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    v = list(range(1, n + 1))
    for j in range(k):
        for l in range(1, n):
            v[l] += v[l - 1]
    print(v[n - 1])