import heapq

heap = []

n = int(input())

for i in range(n):
    heapq.heappush(heap, int(input()))

for i in range(n):
    print(heapq.heappop(heap))
