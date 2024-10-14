class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        num_minus = [-num for num in nums]
        heapq.heapify(num_minus)
        for i in range(k):
            n = heapq.heappop(num_minus)
            ans += n
            heapq.heappush(num_minus, math.floor(n/3))
        return -ans