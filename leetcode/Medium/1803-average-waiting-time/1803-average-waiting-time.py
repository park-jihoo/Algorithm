class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n, t, ans = len(customers), 0, 0
        for start, wait in customers:
            t = max(t + wait, start + wait)
            ans += (t - start) / n
        return ans
