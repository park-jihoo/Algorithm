class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()

        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord("a"), ord(b) - ord("a"))

        result = []
        for c in baseStr:
            smallest = uf.find(ord(c) - ord("a"))
            result.append(chr(smallest + ord("a")))

        return "".join(result)
