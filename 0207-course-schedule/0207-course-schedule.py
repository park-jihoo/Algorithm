class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
            indegree[p[1]] += 1

        result = []
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            result.append(node)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return len(result) == numCourses
