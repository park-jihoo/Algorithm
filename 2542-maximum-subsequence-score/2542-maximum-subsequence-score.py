import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        zipped = sorted(
            [(num2, num1) for num1, num2 in zip(nums1, nums2)], reverse=True
        )
        answer, temp = 0, 0
        heap = []
        for a, b in zipped:
            heapq.heappush(heap, b)
            temp += b
            if len(heap) > k:
                temp -= heapq.heappop(heap)
            if len(heap) == k:
                answer = max(answer, temp * a)
        return answer
