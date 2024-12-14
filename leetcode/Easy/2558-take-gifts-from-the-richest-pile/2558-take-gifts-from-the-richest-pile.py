class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            richest = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(richest)))
        return -sum(gifts)
