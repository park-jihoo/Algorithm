from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        answer = []
        for idx, val in enumerate(equations):
            x, y = val
            graph[x][y] = values[idx]
            graph[y][x] = 1 / values[idx]
        for x, y in queries:
            if x not in graph.keys() or y not in graph.keys():
                answer.append(-1.0)
                continue
            
            q = deque([x])
            visited = set([x])
            par = {x: None}
            flag = False
            while q:
                now = q.pop()
                if now == y:
                    val = 1.0
                    while par[now] is not None:
                        val *= (graph[par[now]][now])
                        now = par[now]
                    answer.append(val)
                    flag = True
                    break
                for child in graph[now].keys():
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
                        par[child] = now
            if not flag:
                answer.append(-1.0)
        return answer