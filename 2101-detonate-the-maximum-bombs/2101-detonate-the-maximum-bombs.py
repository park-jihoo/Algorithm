import math
from collections import defaultdict, deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                distance = sqrt(
                    (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                )
                if distance <= bombs[i][2]:
                    graph[i].append(j)
                if distance <= bombs[j][2]:
                    graph[j].append(i)

        answer = 0
        for idx, bomb in enumerate(bombs):
            visited = [0] * len(bombs)
            q = deque([idx])
            visited[idx] = 1
            while q:
                node = q.popleft()
                for child in graph[node]:
                    if visited[child] == 0:
                        q.append(child)
                        visited[child] = 1
            answer = max(answer, sum(visited))
        return answer
