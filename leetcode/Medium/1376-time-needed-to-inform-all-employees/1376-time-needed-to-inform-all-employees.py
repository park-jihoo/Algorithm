from collections import defaultdict, deque


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        answer = 0
        if n == 1:
            return 0
        graph = defaultdict(list)
        for idx, val in enumerate(manager):
            if val != -1:
                graph[val].append(idx)
        q = deque([headID])
        informed = [False] * n
        informed[headID] = True
        while q:
            node = q.popleft()
            for child in graph[node]:
                if not informed[child]:
                    informed[child] = True
                    informTime[child] += informTime[node]
                    q.append(child)
        return max(informTime)
