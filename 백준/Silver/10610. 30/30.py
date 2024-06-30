N = input()

N = [int(i) for i in N]

if 0 not in N or sum(N) % 3 != 0:
    print(-1)
else:
    N = sorted(N, reverse=True)
    for i in N:
        print(i, end='')