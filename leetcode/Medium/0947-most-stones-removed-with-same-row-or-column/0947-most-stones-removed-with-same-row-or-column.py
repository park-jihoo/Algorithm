class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowd, cold = defaultdict(set), defaultdict(set)
        for idx, (x, y) in enumerate(stones):
            rowd[x].add(idx)
            cold[y].add(idx)
        graph = defaultdict(set)
        for idx, (x, y) in enumerate(stones):
            graph[idx].update(rowd[x])
            graph[idx].update(cold[y])
            graph[idx].remove(idx)
        
        visited = [False]*len(stones)

        answer = len(stones)
        for idx in range(len(stones)):
            if not visited[idx]:
                answer -= 1
                q = [idx]
                while q:
                    node = q.pop()
                    if not visited[node]:
                        visited[node] = True
                        q.extend(graph[node])
        return answer