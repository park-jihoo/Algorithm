from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for dot in range(len(graph)):
            if colors[dot] == 0:
                colors[dot] = 1
                queue = deque([dot])

                while queue:
                    node = queue.pop()
                    for child in graph[node]:
                        if colors[child] == 0:
                            colors[child] = (colors[node]%2)+1
                            queue.append(child)
                        elif colors[child] == colors[node]:
                            return False
        return True