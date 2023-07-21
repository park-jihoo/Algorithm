class Solution:
    def dfs(self, n, graph, visited):
        result = 0
        q = [n]
        while q:
            node = q.pop()
            if not visited[node]:
                visited[node] = True
                result += 1
                q.extend(graph[node])
        return result

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {x: list() for x in range(n)}
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        visited = [False for _ in range(n)]
        temp2 = n
        answer = 0
        for i in range(n):
            if not visited[i]:
                cnt = self.dfs(i, graph, visited)
                answer += cnt * (temp2 - cnt)
                temp2 -= cnt
        return answer
