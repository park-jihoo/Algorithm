class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indeg = [0] * n
        graph = defaultdict(list)
        ans = [set([]) for _ in range(n)]

        for s, e in edges:
            indeg[e] += 1
            graph[s].append(e)
            ans[e].add(s)

        vlist = [i for i in range(n) if indeg[i] == 0]

        while len(vlist) > 0:
            v = vlist.pop()
            for u in graph[v]:
                indeg[u] -= 1
                ans[u] |= ans[v]
                if indeg[u] == 0:
                    vlist.append(u)

        return [sorted(list(a)) for a in ans]
