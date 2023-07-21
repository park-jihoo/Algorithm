class Solution:
    def dfs(self, visited, graph, i):
        if visited[i] == 2:
            return True
        if visited[i] == 1:
            return False
        visited[i] = 1
        for v in graph[i]:
            if not self.dfs(visited, graph, v):
                return False
        visited[i] = 2
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False for _ in range(len(graph))]
        for i in range(len(graph)):
            self.dfs(visited, graph, i)

        return [x for x in range(len(graph)) if visited[x] == 2]
