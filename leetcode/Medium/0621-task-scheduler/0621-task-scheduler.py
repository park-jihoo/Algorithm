class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = list(Counter(tasks).values())
        m = max(d)
        cnt = d.count(m)
        return max(len(tasks), (m - 1) * (n + 1) + cnt)
