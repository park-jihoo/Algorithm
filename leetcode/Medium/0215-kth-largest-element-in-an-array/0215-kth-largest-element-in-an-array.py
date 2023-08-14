class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            heapq.heappush(arr, num)
        return heapq.nlargest(k, arr)[-1]
