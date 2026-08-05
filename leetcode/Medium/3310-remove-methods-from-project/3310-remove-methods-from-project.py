class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for s, e in invocations:
            graph[s].append(e)
        ans = []
        visited = set()
        queue = deque([k])
        while queue:
            cur = queue.pop()
            visited.add(cur)
            for node in graph[cur]:
                if node not in visited:
                    queue.append(node)

        ans = []
        for method in range(n):
            if method in visited:
                continue
            for node in graph[method]:
                if node in visited:
                    return list(range(n))
            ans.append(method)
        return ans
