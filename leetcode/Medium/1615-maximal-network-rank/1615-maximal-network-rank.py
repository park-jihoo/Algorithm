class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in roads:
            graph[start].append(end)
            graph[end].append(start)
        answer = 0
        for i in range(n):
            for j in range(i + 1, n):
                iset = set([(i, x) for x in graph[i]])
                jset = set([(j, x) for x in graph[j] if x != i])
                answer = max(len(iset) + len(jset), answer)
        return answer
