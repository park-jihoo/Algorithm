class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        ops, r = 0, 0
        heap = []
        delta = [0] * (len(nums) + 1)
        for l, elem in enumerate(nums):
            ops += delta[l]
            while r < len(queries) and queries[r][0] == l:
                heapq.heappush(heap, -queries[r][1])
                r += 1
            while ops < elem:
                if not heap or -heap[0] < l:
                    return -1
                delta[1 - heapq.heappop(heap)] -= 1
                ops += 1
        return len(heap)
