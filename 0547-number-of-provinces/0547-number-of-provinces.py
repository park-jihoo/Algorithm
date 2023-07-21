from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        answer = 0
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                answer += 1
                while q:
                    node = q.popleft()
                    for idx, child in enumerate(isConnected[node]):
                        if idx != node and child == 1 and not visited[idx]:
                            visited[idx] = True
                            q.append(idx)
        return answer
