# acmicpc 22860
from collections import defaultdict, deque

n, m = map(int, input().split())

folders, files = defaultdict(list), defaultdict(list)

for _ in range(n + m):
    p, f, c = input().split()
    if c == "1":
        folders[p].append(f)
    else:
        files[p].append(f)

q = int(input())

for _ in range(q):
    query = input().split("/")
    queue = deque([query[-1]])
    file = []
    while queue:
        cur = queue.popleft()
        if cur in folders:
            queue.extend(folders[cur])
        if cur in files:
            file.extend(files[cur])
    print(f"{len(set(file))} {len(file)}")
