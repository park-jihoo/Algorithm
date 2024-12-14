class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(pq)
        marked = [False] * len(nums)
        ans = 0
        while pq:
            val, idx = heapq.heappop(pq)
            if marked[idx]:
                continue
            ans += val
            marked[idx] = True
            if idx >= 1:
                marked[idx - 1] = True
            if idx < len(nums) - 1:
                marked[idx + 1] = True
        return ans
