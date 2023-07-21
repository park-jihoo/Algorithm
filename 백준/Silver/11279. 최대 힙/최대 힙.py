import heapq
from sys import stdin

heap = []
heapq.heapify(heap)
n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())
    if x == 0 and not heap:
        print(0)
    elif x == 0:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
