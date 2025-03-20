class unionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[py] < self.rank[px]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf, weights = unionFind(n), [(1<<32)-1 for _ in range(n)]
        for x, y, e in edges:
            uf.union(x, y)
        for x, y, e in edges:
            weights[uf.find(x)] &=e
        ans = []
        for x, y in query:
            if uf.find(x) == uf.find(y):
                ans.append(weights[uf.find(x)])
            else:
                ans.append(-1)
        return ans
            