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


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n)
        for x, y in edges:
            uf.union(x, y)

        cntr = Counter([uf.find(i) for i in range(n)])
        cntr2 = Counter([uf.find(x) for x, y in edges])
        ans = 0
        for key, val in cntr.items():
            if cntr2[key] == val * (val - 1) // 2:
                ans += 1

        return ans
