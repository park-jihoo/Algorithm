n = int(input())
pre = [int(input()) for x in range(n)]

pre.sort()

answer = 0

for i in range(n):
    answer += abs(i + 1 - pre[i])

print(answer)
