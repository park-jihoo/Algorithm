import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Easy Good! Array Heap
        heap = []

        for stone in stones:
            heapq.heappush(heap, (-stone, stone))

        while True:
            if len(heap) == 0:
                return 0
            if len(heap) == 1:
                return heap[0][1]
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if not a[1] == b[1]:
                val = a[1] - b[1]
                heapq.heappush(heap, (-val, val))
            
        return 0