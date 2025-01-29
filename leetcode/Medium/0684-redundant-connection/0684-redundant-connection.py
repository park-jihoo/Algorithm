class Solution:
    # unionfind
    def find_root(self, node):
        if self.root[node] != node:
            self.root[node] = self.find_root(self.root[node])
        return self.root[node]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.root = list(range(len(edges)+1))

        for s, e in edges:
            r1, r2 = self.find_root(s), self.find_root(e)
            if r1 == r2:
                return [s, e]
            self.root[r2] = r1