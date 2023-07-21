from collections import deque

n, k = map(int, input().split())

q = deque(list(range(1, n + 1)))
a = []

for i in range(n):
    for j in range(k):
        temp = q.popleft()
        if j == k - 1:
            a.append(str(temp))
        else:
            q.append(temp)

print("<" + ", ".join(a) + ">")
