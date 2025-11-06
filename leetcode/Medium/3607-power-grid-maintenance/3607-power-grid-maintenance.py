class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # connected component를 만들어서, online 중 가장 작은 값을 찾아내라
        uf = UnionFind(c)
        for a, b in connections:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(1, c + 1):
            heapq.heappush(groups[uf.find(i)], i)

        offline = set()
        ans = []

        for k, v in queries:
            root = uf.find(v)

            if k == 1:
                if v not in offline:
                    ans.append(v)
                    continue

                heap = groups[root]
                while heap and heap[0] in offline:
                    heapq.heappop(heap)

                if not heap:
                    ans.append(-1)
                else:
                    ans.append(heap[0])

            elif k == 2:
                offline.add(v)

        return ans
