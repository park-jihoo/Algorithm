class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        for i in range(k):
            val, idx = heapq.heappop(heap)
            heapq.heappush(heap, (val * multiplier, idx))
        ans = [0] * len(nums)
        for val, idx in heap:
            ans[idx] = val
        return ans
