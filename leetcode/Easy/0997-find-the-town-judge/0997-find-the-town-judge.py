class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph_a = defaultdict(set)
        graph_b = defaultdict(set)
        for a, b in trust:
            graph_a[a].add(b)
            graph_b[b].add(a)
        for i in range(1, n + 1):
            if len(graph_a[i]) == 0 and len(graph_b[i]) == n - 1:
                return i
        return -1
