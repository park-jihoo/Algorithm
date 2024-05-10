class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lst = [(0, 0, 0)] * k
        for i in range(len(arr) - 1, 0, -1):
            for j in range(min(k, len(arr[:i]))):
                heapq.heappushpop(lst, (arr[i] / arr[j], arr[i], arr[j]))
        ans = heapq.heappop(lst)
        return [ans[2], ans[1]]
