class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        answer = 0
        i = 0
        j = len(costs) - 1
        heap1, heap2 = [], []
        for idx in range(k):
            while len(heap1) < candidates and i <= j:
                heapq.heappush(heap1, costs[i])
                i+=1
            while len(heap2) < candidates and i <= j:
                heapq.heappush(heap2, costs[j])
                j -=1
            if not heap1:
                answer += heapq.heappop(heap2)
            elif not heap2:
                answer += heapq.heappop(heap1)
            elif heap1[0] <= heap2[0]:
                answer += heapq.heappop(heap1)
            else:
                answer += heapq.heappop(heap2)
        return answer