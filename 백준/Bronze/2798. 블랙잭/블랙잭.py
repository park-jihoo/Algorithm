n, m = map(int, input().split())

cards = [int(x) for x in input().split()]

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = cards[i]+cards[j]+cards[k]
            if s<=m:
                answer = max(s, answer)

print(answer)