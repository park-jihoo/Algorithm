from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {x: list() for x in range(n)}
        lookup = set()
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)
            lookup.add(s*n+e)
        result = 0
        q = deque([(-1, 0)])
        while q:
            parent, node = q.pop()
            if parent*n+node in lookup:
                result+=1
            for i in reversed(graph[node]):
                if i == parent:
                    continue
                q.append((node, i))
        return result