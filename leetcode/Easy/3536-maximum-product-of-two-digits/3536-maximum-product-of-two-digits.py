class Solution:
    def maxProduct(self, n: int) -> int:
        pq = []
        while n:
            n, d = divmod(n, 10)
            heapq.heappush(pq, -d)
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        return a * b
