import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq = [float("-inf")] * k
        for n in nums:
            if n > self.pq[0]:
                heapq.heapreplace(self.pq, n)

    def add(self, val: int) -> int:
        if val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
