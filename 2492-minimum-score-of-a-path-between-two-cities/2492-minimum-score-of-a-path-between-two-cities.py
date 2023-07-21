from collections import deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {x: set() for x in range(n + 1)}
        score = [10**5 for x in range(n + 1)]
        answer = 10**10
        for s, e, d in roads:
            graph[s].add(e)
            graph[e].add(s)
            score[s] = min(d, score[s], score[e])
            score[e] = score[s]
        q, visited = deque([1]), set()
        while q:
            node = q.pop()
            if node not in visited:
                visited.add(node)
                answer = min(score[node], answer)
                q.extend(graph[node])
        return answer
