class unionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
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
                self.rank[px] +=1

    def connected(self, x, y):
        return self.find(x) == self.find(y) 
            
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted(edgeList, key = lambda x : x[2])
        answer = [False] * len(queries)
        unionfind = unionFind(n)
        i = 0

        sorted_queries = sorted(enumerate(queries), key=lambda x:x[1][2])

        for idx, (u, v, limit) in sorted_queries:
            while i < len(edges) and edges[i][2] < limit:
                unionfind.union(edges[i][0], edges[i][1])
                i+=1
            answer[idx] = unionfind.connected(u, v)

        return answer