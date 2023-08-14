from collections import deque


class Solution:
    def dfs(self, x, graph, visited):
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                self.dfs(i, graph, visited)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        graph = {x: set() for x in range(n)}
        for s, e in connections:
            graph[s].add(e)
            graph[e].add(s)
        visited = [False] * n
        answer = -1
        for computer in range(n):
            if not visited[computer]:
                self.dfs(computer, graph, visited)
                answer += 1
        return answer
