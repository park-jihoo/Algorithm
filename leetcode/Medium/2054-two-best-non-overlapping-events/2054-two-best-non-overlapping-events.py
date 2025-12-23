class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        a, b = 0, 0
        for start, end, time in events:
            while heap and heap[0][0] < start:
                a = max(a, heapq.heappop(heap)[1])
            b = max(a + time, b)
            heapq.heappush(heap, (end, time))
        return b
