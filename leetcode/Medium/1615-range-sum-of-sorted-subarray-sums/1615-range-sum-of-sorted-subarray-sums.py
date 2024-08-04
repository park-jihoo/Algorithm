class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        ans = 0
        for idx in range(1, right + 1):
            x, i = heapq.heappop(heap)
            if idx >= left:
                ans += x
            if i + 1 < len(nums):
                heapq.heappush(heap, (x + nums[i + 1], i + 1))
        return ans % (10**9 + 7)
