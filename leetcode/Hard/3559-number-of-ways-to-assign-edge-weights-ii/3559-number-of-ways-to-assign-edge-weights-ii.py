class LCA:
    def __init__(self, edges, root=1):
        n = len(edges) + 1
        LOG = math.ceil(math.log2(n)) + 1

        self.depth = [0] * (n + 1)
        self.parent = [[0] * LOG for _ in range(n + 1)]
        self.graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self._dfs(root, 0)

        for k in range(1, LOG):
            for node in range(1, n + 1):
                p = self.parent[node][k - 1]
                self.parent[node][k] = self.parent[p][k - 1]

        self.LOG = LOG

    def _dfs(self, node, par):
        self.parent[node][0] = par

        for nxt in self.graph[node]:
            if nxt == par:
                continue

            self.depth[nxt] = self.depth[node] + 1
            self._dfs(nxt, node)

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a

        # raise a to b's depth
        diff = self.depth[a] - self.depth[b]

        for k in range(self.LOG):
            if diff & (1 << k):
                a = self.parent[a][k]

        if a == b:
            return a

        # lift together
        for k in range(self.LOG - 1, -1, -1):
            if self.parent[a][k] != self.parent[b][k]:
                a = self.parent[a][k]
                b = self.parent[b][k]

        return self.parent[a][0]

    def distance(self, a, b):
        c = self.lca(a, b)
        return self.depth[a] + self.depth[b] - 2 * self.depth[c]

MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LCA(edges)
        ans = []
        for x, y in queries:
            if x == y:
                ans.append(0)
                continue
            dist = lca.distance(x, y)
            ans.append(pow(2, dist - 1, MOD))
        return ans
        