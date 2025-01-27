class Solution:
    def topologicalSort(self, graph, indegree):
        result_dict = defaultdict(set)
        q = deque()
        for idx, val in enumerate(indegree):
            if val == 0:
                q.append(idx)
        while q:
            node = q.popleft()
            for i in graph[node]:
                result_dict[i].add(node)
                result_dict[i].update(result_dict[node])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return result_dict

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1

        topSort = self.topologicalSort(adj, indegree)

        return [u in topSort[v] for u, v in queries]