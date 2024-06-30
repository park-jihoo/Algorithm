class Solution:
    def find(self, x, parents):
        if not x == parents[x]:
            parents[x] = self.find(parents[x], parents)
        return parents[x]

    def union(self, x, y, parents):
        x, y = self.find(x, parents), self.find(y, parents)
        if x == y:
            return 0
        parents[x] = y
        return 1

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ret, e1, e2 = 0, 0, 0
        parent_3 = list(range(n + 1))
        for t, u, v in edges:
            if t == 3:
                if self.union(u, v, parent_3):
                    e1 += 1
                    e2 += 1
                else:
                    ret += 1

        parent_1, parent_2 = parent_3[:], parent_3[:]
        for t, u, v in edges:
            if t == 1:
                if self.union(u, v, parent_1):
                    e1 += 1
                else:
                    ret += 1
            elif t == 2:
                if self.union(u, v, parent_2):
                    e2 += 1
                else:
                    ret += 1

        if e1 == e2 and e1 == n - 1:
            return ret
        else:
            return -1
