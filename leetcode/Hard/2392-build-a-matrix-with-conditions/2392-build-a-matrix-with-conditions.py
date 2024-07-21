class Solution:
    def topologicalSort(self, graph, indegree):
        result = []
        q = deque()
        for idx, val in enumerate(indegree):
            if val == 0:
                q.append(idx)
        while q:
            node = q.popleft()
            result.append(node)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return result

    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        ans = [[0] * k for _ in range(k)]
        rowgraph, colgraph = defaultdict(list), defaultdict(list)
        rowindegree, colindegree = [0 for _ in range(k)], [0 for _ in range(k)]
        for s, e in rowConditions:
            rowgraph[s - 1].append(e - 1)
            rowindegree[e - 1] += 1
        for s, e in colConditions:
            colgraph[s - 1].append(e - 1)
            colindegree[e - 1] += 1
        row, col = self.topologicalSort(rowgraph, rowindegree), self.topologicalSort(
            colgraph, colindegree
        )
        if len(row) < k or len(col) < k:
            return []
        row = {val: idx for idx, val in enumerate(row)}
        col = {val: idx for idx, val in enumerate(col)}
        for x in range(k):
            ans[row[x]][col[x]] = x + 1
        return ans
