class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_heap = []
        for idx, val in enumerate(score):
            heapq.heappush(score_heap, (-val, idx))
        ans = [0] * len(score)
        for i in range(len(score)):
            val, idx = heapq.heappop(score_heap)
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(i + 1)
        return ans
